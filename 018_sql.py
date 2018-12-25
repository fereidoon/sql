import sqlite3
dic={'average':"SELECT avg(population) FROM population",
	  'maximum':"SELECT max(population) FROM population",
	  'minimum':"SELECT min(population) FROM population",
	  'sum':"SELECT sum(population) FROM population",
	   'count':"SELECT count(city) FROM population" }

with sqlite3.connect("new.db") as conn:
	c=conn.cursor()
	for key,script in dic.items():
		c.execute(script)
		result=c.fetchall()
		print(result)
		print("the {} is:{}".format(key,result[0]))


