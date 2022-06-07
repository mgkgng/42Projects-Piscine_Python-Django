from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
import psycopg2
from .models import Movies
from .forms import MovieForm

def index(request):
	return HttpResponse("Hello world!")

def init(request):
	conn = psycopg2.connect(database="djangotraining", host="localhost", user="djangouser", password="secret")
	
	with conn.cursor() as curs:
		try:

			curs.execute("""CREATE TABLE IF NOT EXISTS ex07_movies(
				title varchar(64) NOT NULL UNIQUE,
				episode_nb serial PRIMARY KEY,
				opening_crawl text,
				director varchar(32) NOT NULL,
				producer varchar(128) NOT NULL,
				release_date date NOT NULL,
				created timestamptz NOT NULL DEFAULT current_timestamp,
				updated timestamptz NOT NULL DEFAULT current_timestamp
			)""")
			curs.execute("""CREATE OR REPLACE FUNCTION update_changetimestamp_column()
				RETURNS TRIGGER AS $$
				BEGIN
				NEW.updated = now();
				NEW.created = OLD.created;
				RETURN NEW;
				END;
				$$ language 'plpgsql';
				CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE
				ON ex07_movies FOR EACH ROW EXECUTE PROCEDURE
				update_changetimestamp_column();""")
			conn.commit()
			conn.close()
			return HttpResponse("OK")
		except Exception as e:
			return HttpResponse(e)

def populate(request):
	try:
		movielist = [{"title": "The Phantom Menace", "director": "George Lucas", "producer": "Rick McCallum", "release_date": "1999-05-19"},
		{"title": "Attack of the Clones", "director": "George Lucas", "producer": "Rick McCallum", "release_date": "2002-05-16"},
		{"title": "Revenge of the Sith", "director": "George Lucas", "producer": "Rick McCallum", "release_date": "2005-05-19"},
		{"title": "A New Hope", "director": "George Lucas", "producer": "Gary Kurtz, Rick McCallum", "release_date": "1977-05-25"},
		{"title": "The Empire Strikes Back", "director": "Irvin Kershner", "producer": "Gary Kurtz, Rick McCallum", "release_date": "1980-05-17"},
		{"title": "Return of the Jedi", "director": "Richard Marquand", "producer": "Howard G. Kazanjian, George Lucas, Rick McCallum", "release_date": "1983-05-25"},
		{"title": "The Force Awakens", "director": "J. J. Abrams", "producer": "Kathleen Kennedy, J. J. Abrams, Bryan Burk", "release_date": "2015-12-11"}]
		for movieinfo in movielist:
			m = Movies(title=movieinfo["title"], director=movieinfo["director"], producer=movieinfo["producer"], release_date=movieinfo["release_date"])
			m.save()
		return HttpResponse("OK")
	except Exception as e:
		return HttpResponse(e)

def display(request):
	m = Movies.objects.all()
	movielist = []
	for movie in m:
		movielist.append((movie.title, movie.episode_nb, movie.opening_crawl, movie.director, movie.producer, movie.release_date, movie.created, movie.updated))
	if len(movielist) == 0:
		return HttpResponse("No data available")
	return render(request, "ex07/display.html", {"movielist": movielist})

def update(request):
	if request.method == "POST":
		e_nb = request.POST["movies"]
		form = MovieForm(request.POST)
		if form.is_valid():
			Movies.objects.filter(episode_nb=e_nb).update(opening_crawl=form.cleaned_data["opening_crawl"])
			return HttpResponseRedirect("/ex07/update")
	form = MovieForm()
	m = Movies.objects.all()
	movielist = []
	for movie in m:
		movielist.append((movie.title, movie.episode_nb, movie.opening_crawl, movie.director, movie.producer, movie.release_date, movie.created, movie.updated))
	if len(movielist) == 0:
		return HttpResponse("No data available")
	return render(request, "ex07/update.html", {"movielist": movielist, "form": form})
