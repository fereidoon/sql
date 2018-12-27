import sqlite3
with sqlite3.connect("newnum.db") as conn:
	c=conn.cursor()
	while True:
		try:
			user_answer=int(input("what operation do you what to prossess\avarage:1\maximun:2\minimum:3\sum:4\exit:5"))
		except ValueError:
			print("please inter integer value")
			pass	
		if user_answer==1:
			c.execute("SELECT AVG(num) FROM number ")
			re=c.fetchall()
			print("the avarage is:{}".format(re[0]))
		elif user_answer==2:
			c.execute("SELECT MAX(num) FROM number")
			re=c.fetchall()
			print("the maximun is:{}".format(re))
		elif user_answer==3:
			c.execute("SELECT MIN(num) FROM number")
			re=c.fetchall()
			print("the minimum is :{}".format(re))
		elif user_answer==4:
			c.execute("SELECT SUM(num) FROM number")
			re=c.fetchall()
			print("the summation is:{}".format(re))
		elif user_answer==5:
			break
		else:
			pass				
			
		pass