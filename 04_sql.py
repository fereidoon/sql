import csv
import sqlite3
csv_file=csv.reader(open("employees.csv","r"))
with sqlite3.connect("new.db") as conn:
	c=conn.cursor()
#	c.execute("CREATE TABLE employees (firstname TEXT,lastname TEXT)")
	c.executemany("INSERT INTO employees(firstname,lastname) VALUES(?,?)",csv_file)
