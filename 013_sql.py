import sqlite3
cities = [
('Boston', 'MA', 600000),
('Los Angeles', 'CA', 38000000),
('Houston', 'TX', 2100000),
('Philadelphia', 'PA', 1500000),
('San Antonio', 'TX', 1400000),
('San Diego', 'CA', 130000),
('Dallas', 'TX', 1200000),
('San Jose', 'CA', 900000),
('Jacksonville', 'FL', 800000),
('Indianapolis', 'IN', 800000),
('Austin', 'TX', 800000),
('Detroit', 'MI', 700000)
]
with sqlite3.connect("new.db") as conn:
	c=conn.cursor()
	#c.executemany("INSERT INTO population VALUES (?,?,?) ",cities)
	c.execute("SELECT * FROM population WHERE population>1000000")
	list1=c.fetchall()
	for r in list1:
		print(r[0],r[1],r[2])
