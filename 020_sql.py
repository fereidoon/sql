import sqlite3
import random
with sqlite3.connect("newnum.db") as conn:
	c=conn.cursor()
	#c.execute("CREATE TABLE number(num INT)")
	for i in range(0,100):
		int1=random.randint(0,100)
		c.execute("INSERT INTO number VALUES (?)",(int1,))