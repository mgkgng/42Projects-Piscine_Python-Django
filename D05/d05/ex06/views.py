from django.shortcuts import render, HttpResponse, HttpResponseRedirect
import psycopg2
from .forms import MovieForm

def index(request):
	return HttpResponse("Hello world!")

def init(request):
	conn = psycopg2.connect(database="djangotraining", host="localhost", user="djangouser", password="secret")
	
	with conn.cursor() as curs:
		try:
			curs.execute("""CREATE OR REPLACE FUNCTION update_changetimestamp_column()
					RETURNS TRIGGER AS $$
					BEGIN
					NEW.updated = now();
					NEW.created = OLD.created;
					RETURN NEW;
					END;
					$$ language 'plpgsql';""")
			curs.execute("""CREATE TABLE IF NOT EXISTS ex06_movies(
				title varchar(64) NOT NULL UNIQUE,
				episode_nb serial PRIMARY KEY,
				opening_crawl text,
				director varchar(32) NOT NULL,
				producer varchar(128) NOT NULL,
				release_date date NOT NULL,
				created timestamptz NOT NULL DEFAULT NOW(),
				updated timestamptz NOT NULL DEFAULT NOW()
			)""")
			curs.execute("""CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE
				ON ex06_movies FOR EACH ROW EXECUTE PROCEDURE
				update_changetimestamp_column();""")
			conn.commit()
			conn.close()
			return HttpResponse("OK")
		except Exception as e:
			return HttpResponse(e)

def populate(request):
	conn = psycopg2.connect(database="djangotraining", host="localhost", user="djangouser", password="secret")
	with conn.cursor() as curs:
		try:
			curs.execute("""INSERT INTO ex06_movies(title, director, producer, release_date) 
			VALUES
			('The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-05-19'),
			('Attack of the Clones', 'George Lucas', 'Rick McCallum', '2002-05-16'),
			('Revenge of the Sith', 'George Lucas', 'Rick McCallum', '2005-05-19'),
			('A New Hope', 'George Lucas', 'Gary Kurtz, Rick McCallum', '1977-05-25'),
			('The Empire Strikes Back', 'Irvin Kershner', 'Gary Kurtz, Rick McCallum', '1980-05-17'),
			('Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '1983-05-25'),
			('The Force Awakens', 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', '2015-12-11')
			""")
			conn.commit()
			conn.close()
			return HttpResponse("OK")
		except Exception as e:
			return HttpResponse(e)

def display(request):
	conn = psycopg2.connect(database="djangotraining", host="localhost", user="djangouser", password="secret")
	with conn.cursor() as curs:
		try:
			movielist = []
			curs.execute("SELECT * FROM ex06_movies")
			r = curs.fetchall()
			if len(r) == 0:
				return HttpResponse("No data available")
			for tr in r:
				movielist.append(tr)
			return render(request, "ex06/display.html", {"movielist": movielist})
		except Exception as e:
			return HttpResponse(e)

def update(request):
	conn = psycopg2.connect(database="djangotraining", host="localhost", user="djangouser", password="secret")
	with conn.cursor() as curs:
		try:
			if request.method == "POST":
				e_nb = request.POST["movies"]
				form = MovieForm(request.POST)
				if form.is_valid():
					curs.execute("DELETE FROM ex04_movies WHERE episode_nb=" + e_nb)
					conn.commit()
					conn.close()
					return HttpResponseRedirect("/ex04/remove")
				else:
					form = MovieForm()
			movielist = []
			curs.execute("SELECT * FROM ex06_movies")
			r = curs.fetchall()
			if len(r) == 0:
				return HttpResponse("No data available")
			for tr in r:
				movielist.append(tr)
			return render(request, "ex06/display.html", {"movielist": movielist})
		except Exception as e:
			return HttpResponse(e)

