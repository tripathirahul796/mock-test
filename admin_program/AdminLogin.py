from tkinter import *
import tkinter as tk
import mysql.connector
from tkinter import messagebox
class AdminLogin:
	
	def __init__(self):
		mydb = mysql.connector.connect(
		  host="localhost",
		  user="root",
		  passwd="rahul123",
		  database="OnlineTest"
		) 
		self.mycursor = mydb.cursor()

		self.top=tk.Tk()
		self.top.geometry("1200x700") 
		self.top.title("Online Mock Test  ( Admin Login)")
		self.top.resizable(0,0)
		self.num1=tk.StringVar()
		self.num2=tk.StringVar()

		main_frame=Frame(self.top,bg="white").pack(fill=BOTH,expand=YES)
		login_img=PhotoImage(file="logo//login-admin.png")
		img_label=Label(main_frame,image=login_img)
		img_label.place(x=420,y=100)
		user_lbl=Label(img_label,text="User ID*",font=("Time 10 bold"),bg="white").place(x=25,y=198)
		user_name=Entry(img_label,textvariable=self.num1,bd=2,relief=GROOVE,width=32,font=29)
		user_name.focus_set()
		user_name.place(x=25,y=218,height=40)
		paswd_lbl=Label(img_label,text="Password*",font="Time 10 bold",bg="white").place(x=25,y=268)
		password=Entry(img_label,textvariable=self.num2,show="*",bd=2,relief=GROOVE,width=32,font=29).place(x=25,y=288,height=40)
		login_btn=Button(img_label,text="Login",bg="green",fg="white",width=23,font=("Time 16"),command=self.display).place(x=25,y=350,height=42)
		
		self.top.bind('<Return>',lambda event:self.display())
		self.top.mainloop()

	def display(self):

		sql=("select * from AdminInfo where user_id=%s and paswd=%s ")
		id=self.num1.get()
		paswd=self.num2.get()
		

		if id=="":
			messagebox.showwarning("Admin Login","Please Enter User ID")
		elif paswd=="":
			messagebox.showwarning("Admin Login","Please Enter Password")
		else:
			self.mycursor.execute(sql,[id,paswd])
			record=self.mycursor.fetchone()
			if record:
				
				self.top.destroy()
				import AdminControl as ac
				admin=ac.AdminControl(self.num1.get())
				
			else:
				messagebox.showwarning("Admin Login","Wrong User ID or Password")
					
	
		
adminlogin=AdminLogin()



