from tkinter import *
import tkinter as tk
import mysql.connector
from tkinter import messagebox
from tkinter import simpledialog
from PIL import Image,ImageTk
import base64
import io

class StudentLogin:
	
	def __init__(self,ip_var,paper_id):
		self.ip_var=ip_var
		self.paper_id=paper_id
		mydb = mysql.connector.connect(
		  host=ip_var,#localhost
		  user="rahul",
		  passwd="rahul123",
		  database="OnlineTest"
		)
		self.mycursor = mydb.cursor()		
		self.top=tk.Tk()
		self.top.geometry("1200x700") 
		self.top.resizable(0,0)

		original_logo=Image.open("logo//app_logo.png")
		logo=ImageTk.PhotoImage(original_logo)
		#self.top.iconphoto(False,logo)
		self.top.title("Online Mock Test  ( Student Login)")
		self.num1=tk.StringVar()
		self.num2=tk.StringVar()

		"""self.show_paswd_img=PhotoImage(file="img//show.png")
		self.hide_pass=PhotoImage(file="img//hide_pass.png")"""


		main_frame=Frame(self.top,bg="white").pack(fill=BOTH,expand=YES)
		
		login_img=PhotoImage(file="img//login-admin.png")
		img_label=Label(main_frame,image=login_img)
		img_label.place(x=420,y=100)
		email_lbl=Label(img_label,text="Email ID*",font=("Time 9 bold"),bg="white").place(x=25,y=198)
		user_name=Entry(img_label,textvariable=self.num1,bd=2,relief=GROOVE,width=32,font=29)
		user_name.focus_set()
		user_name.place(x=25,y=218,height=30)
		dob_lbl=Label(img_label,text="DOB(DD/MM/YYYY)*",font="Time 9 bold",bg="white").place(x=25,y=258)
		self.password=Entry(img_label,textvariable=self.num2,bd=2,relief=GROOVE,width=32,font=29)#,show="*"
		self.password.place(x=25,y=278,height=30)
		
		login_btn=Button(img_label,text="Login",bg="green",fg="white",width=23,font=("Time 16"),command=self.display).place(x=25,y=330,height=30)
		new_user=Button(img_label,text="New User?  SignUp here",command=self.stdnReg,bd=0,relief=GROOVE,font=("Time 12 underline "),bg="white",fg="blue").place(x=25,y=380)
		
		self.top.bind('<Return>',lambda event:self.display())
		self.top.mainloop()
		
		
		
	def show_hide_psd(self):
		if(self.check_var.get()):
			self.password.config(show="")
		else:
			self.password.config(show="*")  



	def display(self):
		

		sql=("select * from StudentInfo where email=%s and dob=%s ")
		email=self.num1.get()
		#print(id)
		dob=self.num2.get()
		

		if email=="":
			messagebox.showwarning("Student Login","Please Enter Email ID")
			
		elif dob=="":
			messagebox.showwarning("Student Login","Please Enter Date OF Birth")
			
		else:
			
			self.mycursor.execute(sql,[email,dob])
			record=self.mycursor.fetchone()
			
			if record:
				sql2="select * from result where stdn_email=%s and paper_id=%s"
				self.mycursor.execute(sql2,[email,self.paper_id])
				check_exist=self.mycursor.fetchone()
				#print(check_exist)
				if check_exist==None:
					stdn_img=base64.b64decode(record[9])
					img_file=bytes(stdn_img)
					stdn_email=record[2]
					sign=base64.b64decode(record[14])
					sign_file=bytes(sign)
					stdn_sign=record[2]+"sign"
					self.write_file(img_file,"stdn_img// "+stdn_email+".png")
					self.write_file(sign_file,"stdn_img// "+stdn_sign+".png")

					self.top.destroy()
					import StudentExam as stdn_exam
					obj=stdn_exam.StudentExam(self.ip_var,self.paper_id,email)

				else:
					
					
					messagebox.showerror("Error","You have already taken this exam. Please select another exam!!")
					self.top.destroy()
					import Connection
					#admin=ac.AdminControl()
			else:
				messagebox.showwarning("Student Login","Wrong User Email or DOB")
				
	def write_file(self,data, filename):
		
	# Convert binary data to proper format and write it on Hard Disk
		with open(filename, 'wb') as file:
			file.write(data)
	def stdnReg(self):
		self.top.destroy()
		import StudentRegister as obj
		reg_obj=obj.StudentReg(self.ip_var,self.paper_id)
		adminlogin=StudentLogin(self.ip_var,self.paper_id)
#adminlogin=StudentLogin()



