import sqlite3
with sqlite3.connect("new.db") as conn:
	c=conn.cursor()
	c.execute("SELECT firstname,lastname FROM employees")
	list1=c.fetchall()
	print(list1)
	for r in list1:
		print(r[0],r[1])