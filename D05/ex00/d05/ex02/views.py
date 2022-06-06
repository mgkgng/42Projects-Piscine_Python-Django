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
		m = Movies()
		m.save()
		return HttpResponse("OK")
	except Exception as e:
		return HttpResponse(e)

def display(request):
	movielist = Movies.objects.all()
	if len(movielist) == 0:
		return HttpResponse()
	return render(request, "ex02/display.html", {"movielist": movielist})