import sqlite3
dic={'Ford_Focus':"SELECT count(order_date) FROM orders WHERE make='Ford' AND model='Focus'",
'Honda_civic':"SELECT count(order_date) FROM orders WHERE make='Honda' AND model='Civic'",
'Ford_Ranger':"SELECT count(order_date) FROM orders WHERE make='Ford' AND model='Ranger'",
'Honda_Acord':"SELECT count(order_date) FROM orders WHERE make='Honda' AND model='Accord'",
'Ford_Avenger':"SELECT count(order_date) FROM orders WHERE make='Ford' AND model='Avenger'"}
with sqlite3.connect("cars.db") as conn:
	c=conn.cursor()
	for key,script in dic.items():
		c.execute(script)
		result=c.fetchall()
		print("{} order count is:{}".format(key,result[0]))