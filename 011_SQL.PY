import sqlite3
with sqlite3.connect("cars.db") as conn:
	c=conn.cursor()
	c.execute("UPDATE inventory SET quantity=70 WHERE make='Ford'AND model='Focus'")
	c.execute("UPDATE inventory SET quantity=700 WHERE make='Honda' AND model='avelon'")
	c.execute("UPDATE inventory SET quantity=9999 WHERE quantity=11")
	c.execute("SELECT * FROM inventory")
	for r in c.fetchall():
		print (r)