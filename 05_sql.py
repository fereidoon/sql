import sqlite3
conn=sqlite3.connect("new.db")
c=conn.cursor()
try:
	c.execute("INSERT INTO populations VALUES ('New York City','NY',8400000)")
	C.execute("INSERT INTO populations VALUES('San	Francisco','CA',800000)")
	c.commit()
except sqlite3.OperationalError:
	print("oops somting went error")
	conn.close()
