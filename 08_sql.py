#'New	York	Cit y
import 	sqlite3
with sqlite3.connect("new.db") as conn:
	c=conn.cursor()
	c.execute("UPDATE population set population=9000000 WHERE city='New York City'")
	c.execute("DELETE FROM population WHERE City='Boston'")
	print("\n NEW DATA: \n")
	c.execute("SELECT city,state,population FROM population")
	list1=c.fetchall()
	for r in list1:
		print(r[0],r[1],r[2])

