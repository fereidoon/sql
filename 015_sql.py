import sqlite3
with sqlite3.connect("new.db") as conn:
	c=conn.cursor()
	c.execute("SELECT population.population, population.city ,regions.region FROM population,regions WHERE \
		population.city=regions.city")
	list1=c.fetchall()
	for r in list1:
		print(r)