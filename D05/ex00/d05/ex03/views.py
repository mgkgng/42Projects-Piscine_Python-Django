from django.shortcuts import render, HttpResponse
import psycopg2
from .models import Movies

def init(request):
	conn = psycopg2.connect(database="djangotraining", host="localhost", user="djangouser", password="secret")
	
	with conn.cursor() as curs:
		try:
			curs.execute("""CREATE TABLE ex02names(
				title varchar(64) NOT NULL UNIQUE
				episode_nb serial PRIMARY KEY,
				opening_crawl text,
				director varchar(32) NOT NULL,
				producer varchar(128) NOT NULL,
				release_date date NOT NULL
			)""")
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
	movielist = Movies.objects.all()
	if len(movielist) == 0:
		return HttpResponse("No data available")
	return render(request, "ex02/display.html", {"movielist": movielist})