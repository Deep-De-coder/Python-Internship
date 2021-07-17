from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import matplotlib.pyplot as plt
import requests
import bs4
import pandas as pd 
import sqlite3

def f1():
	main_window.withdraw()
	add_window.deiconify()

def f2():
	add_window.withdraw()
	main_window.deiconify()


def f3():
	main_window.withdraw()
	view_window.deiconify()
	view_window_st_data.delete(1.0,END)
	info=""
	con = None
	try:
		con = connect("kit.db")
		cursor= con.cursor()
		sql ="create table student(rno int primary key, name text, marks int)"
		sql = "select * from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		if data == []:
			showerror("Issue", "No record available")
			if con is not None:
				con.close()
		else:
			for d in data:
				info = info + " rno: " + str(d[0]) + " name: " + str(d[1]) + " marks: " + str(d[2]) + "\n"
			view_window_st_data.insert(INSERT, info)
	except Exception as e:
		showerror("Issue",e)
	finally:
		if con is not None:
			con.close()


def f4():
	view_window.withdraw()
	main_window.deiconify()

	
def f5():

	if (add_window_ent_rno.get() == "" or add_window_ent_name.get() == "" or add_window_ent_marks.get() == ""):
		showerror("Issue!", "Please fill all the details")
	elif add_window_ent_rno.get()[0] == "-" :
		showerror("Issue!", "Roll number can't be negative")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
	elif (add_window_ent_rno.get().isdecimal() == False):
		showerror("Issue!", "Roll number can have integers only")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
	elif (len(add_window_ent_name.get()) < 2):
		showerror("Issue!", "Name can't consist of only one alphabet")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
	elif ((((add_window_ent_name.get()).replace(" ","")).isalpha()) == False):
		showerror("Issue!", "Name can't consist of digits")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
	elif add_window_ent_marks.get()[0] == "-" :
		showerror("Issue!", "Marks can't be negative")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
	elif (add_window_ent_marks.get().isdecimal() == False):
		showerror("Issue!", "Marks can be integers only")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
	elif int(add_window_ent_marks.get()) > 100:
		showerror("Issue!", "Marks can't be greater than 100")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)	
	else :
		con=None
		try:
			con = connect("kit.db")
			cursor= con.cursor()
			sql = "insert into student values('%d', '%s' , '%d' )"
			rno = int(add_window_ent_rno.get())
			name= add_window_ent_name.get()
			marks = int(add_window_ent_marks.get())
			cursor.execute(sql % (rno, name ,marks))
			showinfo("Success","record added")				
			con.commit()
			add_window_ent_rno.delete(0,END)
			add_window_ent_name.delete(0,END)
			add_window_ent_marks.delete(0,END)
			add_window_ent_rno.focus()
		except Exception as e:
			showerror("Error",e)
			con.rollback()
		finally:
			if con is not None:
				con.close()



def f6():
	main_window.withdraw()
	update_window.deiconify()

def f7():
	update_window.withdraw()
	main_window.deiconify()

def f8():
	main_window.withdraw()
	delete_window.deiconify()

def f9():
	delete_window.withdraw()
	main_window.deiconify()

def f10():
	if (update_window_ent_rno.get() == "" or update_window_ent_name.get() == "" or update_window_ent_marks.get() == ""):
		showerror("Issue!", "Please fill all the details")
	elif update_window_ent_rno.get()[0] == "-" :
		showerror("Issue!", "Roll number can't be negative")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
	elif ((update_window_ent_rno.get().isdecimal()) == False):
		showerror("Issue!", "Roll number can have integers only")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
	elif (len(update_window_ent_name.get()) < 2):
		showerror("Issue!", "Name can't consist of only one alphabet")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
	elif ((((update_window_ent_name.get()).replace(" ","")).isalpha()) == False):
		showerror("Issue!", "Name can't consist of digits")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
	elif update_window_ent_marks.get()[0] == "-" :
		showerror("Issue!", "Marks can't be negative")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
	elif (update_window_ent_marks.get().isdecimal() == False):
		showerror("Issue!", "Marks can be integers only")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
	elif int(update_window_ent_marks.get()) > 100:
		showerror("Issue!", "Marks can't be greater than 100")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
	else:
		con= None
		try:
			con = connect("kit.db")
			cursor = con.cursor()	
			rno = int(update_window_ent_rno.get())		
			name= update_window_ent_name.get()
			marks = int(update_window_ent_marks.get())
			sql ="update student set name = '%s' , marks='%d' where rno ='%d' "
			cursor.execute(sql % (name,marks,rno))
			if cursor.rowcount == 1:
				showinfo("Success","record updated")
				con.commit()
				update_window_ent_rno.delete(0, END)
				update_window_ent_name.delete(0, END)
				update_window_ent_marks.delete(0, END)
			else:
				showerror("Issue","record does not exist")
				update_window_ent_rno.delete(0, END)
				update_window_ent_name.delete(0, END)
				update_window_ent_marks.delete(0, END)
		except Exception as e:
			showerror("Error",e)
		finally:
			if con is not None:
				con.close()

def f11():

	if (delete_window_ent_rno.get() == ""):
		showerror("Issue!", "Please enter roll number")
	elif delete_window_ent_rno.get()[0] == "-" :
		showerror("Issue!", "Roll number can't be negative")
		delete_window_ent_rno.delete(0, END)
	elif delete_window_ent_rno.get().isdecimal() == False:
		showerror("Issue!", "Roll number can be integers only")
		delete_window_ent_rno.delete(0, END)
	else:
		con= None
		try:
			con = connect("kit.db")
			cursor = con.cursor()
			rno = int(delete_window_ent_rno.get())
			sql ="delete from student where rno ='%d' "
			cursor.execute(sql%(rno))
			if cursor.rowcount == 1:
				showinfo("Success","record deleted")
				con.commit()	
				delete_window_ent_rno.delete(0,END)
			else:
				showerror("Error","record does not exist")
				delete_window_ent_rno.delete(0,END)
				delete_window_ent_rno.focus()
		except Exception as e:
			showerror("Error",e)
			con.rollback()
		finally:
			if con is not None:
				con.close()

def chart():
	list_marks = []
	list_names = []	
	con=None
	try:
		con=connect('kit.db')
		cursor=con.cursor()
		sql="select marks from student"
		cursor.execute(sql)
		data=cursor.fetchall()
		for d in data:	
			list_marks.append(int(str(d[0])))
	except Exception as e:
		showerror("Error!", e)
	finally:
		if con is not None:
			con.close()

	con=None
	try:
		con=connect('kit.db')
		cursor=con.cursor()
		sql="select name from student"
		cursor.execute(sql)
		data=cursor.fetchall()
		for d in data:	
			list_names.append(str(d[0]))
	except Exception as e:
		showerror("Error", e)
	finally:
		if con is not None:
			con.close()


	plt.bar(list_names, list_marks, width = 0.5, color = ['red', 'green', 'blue'])
	plt.title("Batch Information!")
	plt.xlabel("Students")
	plt.ylabel("Marks")

	plt.show()			



main_window = Tk()
main_window.title("S. M. S.")
main_window.geometry("500x500+400+100")

f = ('Calibri',18,'bold')
main_window_btn_add = Button(main_window, text="Add",width=10,font=f,command=f1)
main_window_bn_view = Button(main_window,text="View",width=10,font=f,command=f3)
main_window_btn_update = Button(main_window, text="Update",width=10,font=f,command=f6)
main_window_btn_delete = Button(main_window, text="Delete",width=10,font=f,command=f8)
main_window_btn_chart = Button(main_window, text="Charts", width=10 , font=f,command=chart)


wa= "http://www.brainyquote.com/quote_of_the_day"
res =requests.get(wa)
data =bs4.BeautifulSoup(res.text, 'html.parser')
info= data.find('img',{'class':'p-qotd'})
msg=info['alt']

wa = "https://ipinfo.io/"
response = requests.get(wa)
data = response.json()
#print(data)
city_name=data['city']

a1 ="http://api.openweathermap.org/data/2.5/weather?units=metric"
a2= "&q=" + city_name
a3 = "&appid=" + "c6e315d09197cec231495138183954bd"
wa =a1+a2+a3
responce = requests.get(wa)
data =responce.json()
temp =str(data['main']['temp'])

lab1 = Label(main_window, text="Location : "+city_name+"		Temp: "+temp+"\u2103",relief="groove", width=35 ,font=f, anchor="sw")

##lab2 = Label(main_window, text="QOTD: "+msg, anchor="sw",borderwidth=3,relief="groove", width=90 ,font=f, wraplength=0) 

lab3 = Label(main_window, text="QOTD : " + msg, font =f , wraplength = 500,relief="groove")



main_window_btn_add.pack(pady=10)
main_window_bn_view.pack(pady=10)
main_window_btn_update.pack(pady=10)
main_window_btn_delete.pack(pady=10)
main_window_btn_chart.pack(pady=10)
lab1.pack(pady=5)
##lab2.pack(pady=5)

lab3.pack(pady=5,padx=1)
main_window['bg']='light green'


#FOR ADD WINDOW

add_window = Toplevel(main_window)
add_window.title("Add St.")
add_window.geometry("500x500+400+100")


add_window_lbl_rno =Label(add_window ,text="enter rno:",font=f)
add_window_ent_rno =Entry(add_window ,bd=5,font=f)
add_window_lbl_name =Label(add_window ,text="enter name:",font=f)
add_window_ent_name =Entry(add_window ,bd=5,font=f)
add_window_lbl_marks =Label(add_window ,text="enter marks:",font=f)
add_window_ent_marks =Entry(add_window ,bd=5,font=f)
add_window_btn_save= Button(add_window,text="save",width=10 ,font=f,command=f5)
add_window_btn_back= Button(add_window,text="back",width=10 ,font=f,command=f2)


add_window_lbl_rno.pack(pady=10)
add_window_ent_rno.pack(pady=10)
add_window_lbl_name.pack(pady=10)
add_window_ent_name.pack(pady=10)
add_window_lbl_marks.pack(pady=10)
add_window_ent_marks.pack(pady=10) 
add_window_btn_save.pack(pady=10)
add_window_btn_back.pack(pady=10)
add_window['bg']='light blue'

add_window.withdraw()




#FOR VIEW BUTTON

view_window = Toplevel(main_window)
view_window.title("View St.")
view_window.geometry("500x500+400+100")
view_window_st_data = ScrolledText(view_window,width=50,height=20)
view_window_btn_back=Button(view_window,text="back",font=f,command=f4)

view_window_st_data.pack(pady=10)
view_window_btn_back.pack(pady=10)
view_window['bg']='light yellow'

view_window.withdraw()



#FOR UPDATE WINDOW

update_window = Toplevel(main_window)
update_window.title("Update St.")
update_window.geometry("500x500+400+100")


update_window_lbl_rno =Label(update_window ,text="enter rno:",font=f)
update_window_ent_rno =Entry(update_window ,bd=5,font=f)
update_window_lbl_name =Label(update_window ,text="enter name:",font=f)
update_window_ent_name =Entry(update_window ,bd=5,font=f)
update_window_lbl_marks =Label(update_window ,text="enter marks:",font=f)
update_window_ent_marks =Entry(update_window ,bd=5,font=f)
update_window_btn_save= Button(update_window,text="save",font=f,command=f10)
update_window_btn_back= Button(update_window,text="back",font=f,command= f7)


update_window_lbl_rno.pack(pady=10)
update_window_ent_rno.pack(pady=10)
update_window_lbl_name.pack(pady=10)
update_window_ent_name.pack(pady=10)
update_window_lbl_marks.pack(pady=10)
update_window_ent_marks.pack(pady=10) 
update_window_btn_save.pack(pady=10)
update_window_btn_back.pack(pady=10)
update_window['bg']='bisque'

update_window.withdraw()


#FOR DELETE WINDOW

delete_window = Toplevel(main_window)
delete_window.title("Delete St.")
delete_window.geometry("500x500+400+100")


delete_window_lbl_rno =Label(delete_window ,text="enter rno:",font=f)
delete_window_ent_rno =Entry(delete_window ,bd=5,font=f)
delete_window_btn_save= Button(delete_window,text="save",font=f,command=f11)
delete_window_btn_back= Button(delete_window,text="back",font=f,command=f9)

delete_window_lbl_rno.pack(pady=10)
delete_window_ent_rno.pack(pady=10)
delete_window_btn_save.pack(pady=10)
delete_window_btn_back.pack(pady=10)
delete_window['bg']='light blue'

delete_window.withdraw()




main_window.mainloop()


