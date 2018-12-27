import sqlite3
prompt	=	""" Select the	operation	that	you	want	to	perform	[1-5]:
 1.	Average
  2.	Max 
  3.	Min 
  4.	Sum 
  5.	Exit """
with sqlite3.connect("newnum.db") as conn:
	c=conn.cursor()	
	while True:
		user_answer=input(prompt)
		if user_answer in ["1","2","3","4"]:
			operation={1:"avg",2:"max",3:"min",4:"sum"}[int(user_answer)]
			c.execute("SELECT {}(num) FROM number".format(operation))
			ans=c.fetchall()
			print("the {} is:{}".format(operation,ans[0]))
		elif user_answer =="5":
			print("exit")
			break
			


		