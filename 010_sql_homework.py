import	sqlite3
list1=[("Ford","capris",13),("Ford","capris",11),("Ford","capris",20),("Honda","avelon",19),("Honda","avelon",16)]
with sqlite3.connect("cars.db") as conn:
	c=conn.cursor()
	c.executemany("INSERT INTO inventory(make,model,quantity) VALUES(?,?,?)" ,list1)