from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class Connection():
	def __init__(self):

	
		self.root=Tk()
		
		self.root.geometry("500x400")
		self.root.title("Establish Connection")
		self.root.attributes("-toolwindow",1)
		main_frame=Frame(self.root,height=400,width=500,bd=2,bg="white").place(x=0,y=0)
		
		ip_label=Label(main_frame,text="IP Address*",font=("time 9 bold"),bg="white").place(x=80,y=100)
		self.ip_var=StringVar(main_frame)
		ip_entry=Entry(main_frame,textvariable=self.ip_var,width=20,bd=2,relief=GROOVE)
		ip_entry.focus()
		ip_entry.place(x=80,y=120)
		self.paper_id_var=StringVar(main_frame)
		paper_id_lbl=Label(main_frame,text="Paper ID*",font=("time 9 bold"),bg="white").place(x=80,y=180)
		paper_id_entry=Entry(main_frame,textvariable=self.paper_id_var,width=20,bd=2,relief=GROOVE).place(x=80,y=200)
		submit_btn=Button(main_frame,text="Submit",command=self.ip_connection,bg="green",fg="white",font=("time 12")).place(x=130,y=260)

		note=Label(main_frame,text="Note:- Please make sure the IP Address and Paper ID and then establish connection",height=2,bd=2,relief=GROOVE,bg="white",font=("Time 9 bold")).place(x=10,y=360)
		self.root.bind('<Return>', self.ip_connection)
		self.root.mainloop()
	def ip_connection(self,event):
		
		try:
			if  re.match(r'[0-9]+(?:\.[0-9]+){3}', self.ip_var.get()):
				self.connection = mysql.connector.connect(
			  host=self.ip_var.get(),
			  user="rahul",
			  passwd="rahul123",
			  database="OnlineTest"
			)
				if self.connection:#.is_connected():
					self.mycursor = self.connection.cursor()
				
				# check table is exist or not
					#sql= "select * from information_schema.tables where table_name=%s"
					sql="select * from QuestionSeries where paper_id=%s"
					self.mycursor.execute(sql,[self.paper_id_var.get()])
					record=self.mycursor.fetchone()

					if record:
						sql2="select count(*) from "+self.paper_id_var.get()
						self.mycursor.execute(sql2)
						total_ques=self.mycursor.fetchall()
						
						
						if int(record[4])==int(total_ques[0][0]):

							messagebox.showinfo("","Successfully Connected")
							self.root.destroy()
							import StudentLogin as stdn_login
							obj=stdn_login.StudentLogin(self.ip_var.get(),self.paper_id_var.get())
						else:
							messagebox.showerror("Error","This paper is not complete.Please complete the paper.")

					else:
						messagebox.showerror("","This Paper not exist!!")
				

				
			
				else:
					messagebox.showerror("Error",'Invalid IP Address')
			else:
				messagebox.showerror("Error",'Invalid IP Address Format')
		except:
			messagebox.showerror("","Something went wrong!! Try Again!!")
				
			
		
obj=Connection()

