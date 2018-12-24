import sqlite3
with sqlite3.connect("new.db") as conn:
	c=conn.cursor()
	c.execute("SELECT DISTINCT population.city,population.population,regions.region FROM population,regions \
	 WHERE population.city=regions.city ORDER BY population.population ASC")
	row=c.fetchall()
	for r in row:
		print("City: {}".format(r[0]))
		print("Population: {}".format(r[1]))
		print("region: {}".format(r[2]))
		print("")