import psycopg2

if __name__ == "__main__":
	conn = psycopg2.connect(database="basename", host="localhost", user="username", password="password")
	cursor = conn.cursor()

	cursor.execute("""CREATE TABLE ex00names(
		title varchar(64) NOT NULL,
		episode_nb PRIMARY KEY
	)""")