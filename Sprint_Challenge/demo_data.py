# Import Statement
import sqlite3
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

#Create the Table
query = """CREATE TABLE demo (
	s varchar(1),
	x INT,
	y INT
	);"""

curs.execute(query)

#Insert the mock data
query = """INSERT INTO demo
VALUES ('g', 3, 9);"""

curs.execute(query)

query = """INSERT INTO demo
VALUES ('v', 5, 7);"""

curs.execute(query)

query = """INSERT INTO demo
VALUES ('f', 8, 7);"""

curs.execute(query)

#commit the new data
conn.commit()

#How many rows?
query = """SELECT Count(*) FROM demo;"""

curs.execute(query)
print('How many rows?:', curs.fetchall()[0][0])

#Where are x and y at least 5?
query = """SELECT COUNT(*) FROM demo
WHERE (x >=5) AND (y >=5);"""

curs.execute(query)
print('How many rows where by x and y are at least 5?:', curs.fetchall()[0][0])

#How many values are in y
query = """SELECT COUNT(DISTINCT y) FROM demo;"""

curs.execute(query)
print('How many unique y values?:', curs.fetchall()[0][0])