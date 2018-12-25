import sqlite3
with sqlite3.connect("cars.db") as conn:
	c=conn.cursor()
	c.execute("""SELECT inventory.make,inventory.model,inventory.quantity, 
	orders.order_date FROM inventory INNER JOIN orders
	ON 	inventory.model = orders.model""")
	row=c.fetchall()
	for r in row:
		print(r[0],r[1])
		print(r[2])
		print(r[3])
		print()
