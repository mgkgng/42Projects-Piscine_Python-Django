from django.shortcuts import render, HttpResponse, HttpResponseRedirect
import psycopg2

def index(request):
	return HttpResponse("Hello world!")

def init(request):
	conn = psycopg2.connect(database="djangotraining", host="localhost", user="djangouser", password="secret")
	
	with conn.cursor() as curs:
		try:
			curs.execute("""CREATE TABLE IF NOT EXISTS ex08_planet(
				id serial PRIMARY KEY,
				name varchar(64) NOT NULL UNIQUE,
				climate varchar,
				diameter bigint,
				orbital_period bigint,
				population large bigint,
				rotation_period bigint,
				surface_water real,
				terrain varchar(128)
			)""")
			curs.execute("""CREATE TABLE IF NOT EXISTS ex08_people(
				id serial PRIMARY KEY,
				name varchar(64) NOT NULL UNIQUE,
				birth_year varchar(32),
				gender varchar(32),
				eye_color varchar(32),
				hair_color varchar(32),
				height integer,
				mass real,
				homeworld varchar(64) REFERENCES ex08_planet(name)
			)""")
			conn.commit()
			conn.close()
			return HttpResponse("OK")
		except Exception as e:
			return HttpResponse(e)

def populate(request):
	with open("ex08/people.csv") as f_people:
		lines = f_people.readlines()
		people_info = [line.split(' ') for line in lines]
	with open("ex08/planet.csv") as f_planet:
		lines = f_planet.readlines()
		planet_info = [line.split(' ') for line in lines]
	conn = psycopg2.connect(database="djangotraining", host="localhost", user="djangouser", password="secret")
	with conn.cursor() as curs:
		try:
			for elem in people_info:
			curs.execute("""INSERT INTO ex08_planet(name, climate, diameter, orbital_period, population, rotation_period, surface_water, terrain) 
			VALUES
			('The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-05-19'),
			""")
			peopl
			conn.commit()
			conn.close()
			return HttpResponse("OK")
		except Exception as e:
			return HttpResponse(e)