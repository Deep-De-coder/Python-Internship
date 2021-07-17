# Create table
from sqlite3 import*

con= None
try:
	con = connect("kit.db")
	print("DB created/opened")
	cursor = con.cursor()
	sql ="create table student(rno int primary key, name text, marks int)"
	cursor.execute(sql)
	print("Table created")
except Exception as e:
	print("Issue ",e)
finally:
	if con is not None:
		con.close()
		print("DB closed")