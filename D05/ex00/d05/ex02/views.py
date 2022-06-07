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

curr.execute(”””

INSERT INTO basename(key1, key2, key3) VALUES

(value1-1, value1-2, value1-3)

(value2-1, value2-2, value2-3)

“””)


def populate(request):
	conn = psycopg2.connect(database="djangotraining", host="localhost", user="djangouser", password="secret")
	with conn.cursor() as curs:
		try:
			curs.execute("""INSERT INTO djangotraining(title, director, producer, release_date) VALUES
			("The Phantom Menace", "George Lucas", "Rick McCallum", "1999-05-19"),
			("Attack of the Clones", "George Lucas", "Rick McCallum", "2002-05-16"),
			("Revenge of the Sith", "George Lucas", "Rick McCallum", "2005-05-19"),
			("A New Hope", "George Lucas", "Gary Kurtz, Rick McCallum", "1977-05-25"),
			("The Empire Strikes Back", "Irvin Kershner", "Gary Kurtz, Rick McCallum", "1980-05-17"),
			("Return of the Jedi", "Richard Marquand", "Howard G. Kazanjian, George Lucas, Rick McCallum", "1983-05-25"),
			("The Force Awakens", "J. J. Abrams", "Kathleen Kennedy, J. J. Abrams, Bryan Burk", "2015-12-11")
			""")
			conn.commit()
			conn.close()
			return HttpResponse("OK")
		except Exception as e:
			return HttpResponse(e)

def display(request):
	movielist = Movies.objects.all()
	if len(movielist) == 0:
		return HttpResponse("No data available")
	return render(request, "ex02/display.html", {"movielist": movielist})