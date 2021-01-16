from tkinter import *
from tkinter import filedialog
import calendar 
import re
import mysql.connector
from PIL import Image,ImageTk
from datetime import datetime
from tkinter import messagebox
import base64
import io


class StudentReg():
	def __init__(self,ip_var,paper_id):
		self.mydb = mysql.connector.connect(
		  host=ip_var,
		  user="rahul",
		  passwd="rahul123",
		  database="OnlineTest"
		)
		self.mycursor = self.mydb.cursor()
		
		
		self.window = Tk()

		self.window.title("Student Registration")
		#window.overrideredirect(True)
		width=self.window.winfo_screenwidth()/2
		height= self.window.winfo_screenheight()/1.3
		self.window.geometry('%sx%s' % (int(width/1.2), int(height)))
		self.window.resizable(0,0)

		head_frame = Frame(self.window, width = 700, height = 20, highlightbackground = 'black', highlightcolor = 'black', highlightthickness = 1)
		head_frame.pack(side = TOP)

		#make a label for top frame
		lbl = Label(head_frame, text = "Student Registration", bg = "#17A8FF", fg = "white", font = ('arial', 14, 'bold',))
		lbl.grid(column = 0, row = 0)
		lbl.pack(ipady = 4, ipadx = 700)
	
		# making an another frame for user login 

		input_frame = Frame(self.window, width = 1200, height = 700)
		input_frame.pack()

		lbl2 = Label(input_frame, text = "First Name*",font=("Time 9 bold"))
		lbl2.place(x =30,y=10)
		self.fname_var=StringVar(input_frame)
		fname = Entry(input_frame,textvariable=self.fname_var,width = 35,relief=GROOVE,bd=2)
		fname.place(x=30,y=30)
		lbl4 = Label(input_frame, text = "Last Name*",font=("Time 9 bold"))
		lbl4.place(x =300,y=10)
		self.lname_var=StringVar(input_frame)
		lname = Entry(input_frame,textvariable=self.lname_var, width = 35,relief=GROOVE,bd=2)
		lname.place(x =300,y=30)
		
		lble = Label(input_frame, text = "Email*",font=("Time 9 bold"))
		lble.place(x =30,y=70)
		self.email_var=StringVar(input_frame)
		email = Entry(input_frame,textvariable=self.email_var, width = 35,relief=GROOVE,bd=2)
		email.place(x =30,y=90)

		lblm = Label(input_frame, text = "Mobile No.*",font=("Time 9 bold"))
		lblm.place(x =300,y=70)
		self.mobile_var=StringVar(input_frame)
		mobile = Entry(input_frame,textvariable=self.mobile_var, width = 35,relief=GROOVE,bd=2)
		mobile.place(x =300,y=90)

		self.gen_value=StringVar(input_frame)
		lblg = Label(input_frame, text = "Gender*",font=("Time 9 bold"))
		lblg.place(x =30,y=130)
		male = Radiobutton(input_frame, text= "Male", value = "Male",variable=self.gen_value)
		male.place(x =30,y=150)
		female = Radiobutton(input_frame, text= "Female", value = "Female",variable=self.gen_value)
		female.place(x =100,y=150)
		other = Radiobutton(input_frame, text= "Other", value = "Other",variable=self.gen_value)
		other.place(x =170,y=150)
	

		self.dob_var=StringVar(input_frame)
		
		lblb = Label(input_frame, text = "Date Of Birth*",font=("Time 9 bold"))
		lblb.place(x =300,y=130)
		self.dob=Entry(input_frame,textvariable=self.dob_var, width = 35,relief=GROOVE,bd=2)
		self.dob.place(x=300,y=160)
		
		lblrel = Label(input_frame, text = "Religion*",font=("Time 9 bold"))
		lblrel.place(x =30,y=190)
		self.religion_var=StringVar(input_frame)
		religion = Entry(input_frame,textvariable=self.religion_var ,width = 35,relief=GROOVE,bd=2)
		religion.place(x =30,y=210)

		lblnat = Label(input_frame, text = "Nationality*",font=("Time 9 bold"))
		lblnat.place(x =300,y=190)
		self.nationality_var=StringVar(input_frame)
		nationality = Entry(input_frame,textvariable=self.nationality_var, width = 35,relief=GROOVE,bd=2)
		nationality.place(x =300,y=210)
		
		lbli=Label(input_frame,text="Image*",font=("Time 9 bold"))
		lbli.place(x=300,y=250)
		btni = Button(input_frame, text = "Choose file",command=self.openImage)
		btni.place(x =300,y=280)

		self.lblsimg=Label(input_frame,image="")
		self.lblsimg.place(x=385,y=240)
	
		lbl_sign=Label(input_frame,text="Sign*",font=("Time 9 bold"))
		lbl_sign.place(x=300,y=355)
		btn_sign=Button(input_frame,text="Choose Sign",command=self.openSign)
		btn_sign.place(x=300,y=380)
		self.lblsign=Label(input_frame,image="")
		self.lblsign.place(x=385,y=360)


		self.state_var=StringVar(input_frame)
		state_lbl=Label(input_frame,text="State*",font=("Time 9 bold"))
		state_lbl.place(x=30,y=250)
		state_entry=Entry(input_frame,textvariable=self.state_var, width = 35,relief=GROOVE,bd=2)
		state_entry.place(x=30,y=270)

		self.dist_var=StringVar(input_frame)
		dist_lbl=Label(input_frame,text="District*",font=("Time 9 bold"))
		dist_lbl.place(x=30,y=310)
		dist_entry=Entry(input_frame,textvariable=self.dist_var, width = 35,relief=GROOVE,bd=2)
		dist_entry.place(x=30,y=330)

		self.pin_var=StringVar(input_frame)
		pin_lbl=Label(input_frame,text="Pin*",font=("Time 9 bold"))
		pin_lbl.place(x=30,y=370)
		pin_entry=Entry(input_frame,textvariable=self.pin_var, width = 35,relief=GROOVE,bd=2)
		pin_entry.place(x=30,y=390)
		lbla = Label(input_frame, text = "Address*",font=("Time 9 bold"))
		lbla.place(x=30,y=430)
		self.address =Text (input_frame, height=3,width=60,relief=GROOVE,bd=2)
		self.address.place(x=30,y=450)
		btnr = Button (input_frame, text = "Register",command=self.addData, background = "red", foreground= "white",font=("Time 9 bold"))
		btnr.place(x=260,y=515)

		self.img_file=""
		self.sign_file=""
		
		self.window.mainloop()
	
	def openImage(self):
		try:
			self.img_file=filedialog.askopenfilename(initialdir = "Desktop",title = "Select Image",filetypes = (("Image Files","*.png"),("All Files","*.*")))
			self.original_stdn_pic = Image.open(self.img_file)
			resized_stdn_pic = self.original_stdn_pic.resize((80, 80),Image.ANTIALIAS)
			self.stdn_img = ImageTk.PhotoImage(resized_stdn_pic)
			self.lblsimg.config(image=self.stdn_img)
		except:
			messagebox.showwarning("","Please select image file !!")
	def openSign(self):
		try:
			self.sign_file=filedialog.askopenfilename(initialdir = "Desktop",title = "Select Image",filetypes = (("Image Files","*.png"),("All Files","*.*")))
			self.original_stdn_sign = Image.open(self.sign_file)
			resized_stdn_sign = self.original_stdn_sign.resize((80, 50),Image.ANTIALIAS)
			self.stdn_sign = ImageTk.PhotoImage(resized_stdn_sign)
			self.lblsign.config(image=self.stdn_sign)
		except:
			messagebox.showwarning("","Please select sign!!")
	
	
	def convertToBinaryData(self,filename):
	# Convert digital data to binary format 
		with open(filename, 'rb') as file:
			binaryData = file.read()
			encodestring = base64.b64encode(binaryData)

		#return binaryData
		return encodestring
			


	def addData(self):

		try:
			sql="insert into  studentinfo(fname,lname,email,mobile,gender,dob,religion,nationality,state,img,dist,pin,address,reg_date,sign) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
			stdn_pic= self.convertToBinaryData(self.img_file)
			stdn_sign=self.convertToBinaryData(self.sign_file)
		
			self.mycursor.execute(sql,[self.fname_var.get(),self.lname_var.get(),self.email_var.get(),self.mobile_var.get(),\
				self.gen_value.get(),self.dob_var.get(),self.religion_var.get(),self.nationality_var.get(),\
				self.state_var.get(),stdn_pic,self.dist_var.get(),self.pin_var.get(),self.address.get("1.0",END),datetime.now().date(),stdn_sign])		
			self.mydb.commit()# it make database modifiable
			messagebox.showinfo("Status","Successfully Added ")
			self.fname_var.set(""),self.lname_var.set(""),self.email_var.set(""),self.mobile_var.set(""),\
				self.gen_value.set(""),self.dob_var.set(""),self.religion_var.set(""),self.nationality_var.set(""),\
				self.state_var.set(""),self.dist_var.set(""),self.pin_var.set(""),self.lblsimg.config(image=""),self.lblsign.config(image=""),self.address.delete("1.0",END)
			#obj=stdn_login.StudenLogin()
		except:
			messagebox.showwarning("Error","Something Wrong.Please try again!!")			




#obj=StudentReg()


	