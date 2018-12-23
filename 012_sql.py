import sqlite3
with sqlite3.connect("cars.db") as conn:
	c=conn.cursor()
	c.execute("SELECT * FROM inventory WHERE make='Ford'")
	for r in c.fetchall():
		print(r)