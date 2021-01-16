from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import mysql.connector
import socket 

class AddQuestion():
	def __init__(self):
		self.mydb = mysql.connector.connect(
		 host="localhost",
		  user="root",
		  passwd="rahul123",
		  database="OnlineTest"
		)
		self.mycursor = self.mydb.cursor()
		


		window = Tk()

		window.title("Add Questions")
		#window.overrideredirect(True)
		width=window.winfo_screenwidth()/2.2
		height= window.winfo_screenheight()/1.3
		window.geometry('%sx%s' % (int(width/1.2), int(height)))

		head_frame = Frame(window, width = 700, height = 20, highlightbackground = 'black', highlightcolor = 'black', highlightthickness = 1)
		head_frame.pack(side = TOP)

		#make a label for top frame
		lbl = Label(head_frame, text = "Question Management", bg = "#17A8FF", fg = "white", font = ('arial', 14, 'bold',))
		lbl.grid(column = 0, row = 0)
		lbl.pack(ipady = 4, ipadx = 700)
		

		input_frame = Frame(window, width = 1200, height = 700)
		input_frame.pack()

		self.question_no=StringVar(input_frame)
		#self.question=StringVar(input_frame)
		self.option1=StringVar(input_frame)
		self.option2=StringVar(input_frame)
		self.option3=StringVar(input_frame)
		self.option4=StringVar(input_frame)
		self.answer=StringVar(input_frame)
		

		#Sql Query to extract data of paper id & paper name
		self.mycursor.execute("select * from QuestionSeries")#ExamDashboard")
		record=self.mycursor.fetchall()
		paper_id_list=[]
		paper_name_list=[]
		for row in record:
			paper_id_list.append(row[1])
			paper_name_list.append(row[2])
			#print(row[0])
		
		
		lblp = Label(input_frame, text = "Paper ID*",font=("Time 9 bold"))
		lblp.place(x =30,y=10)
		self.paper_id_var=StringVar(input_frame)
		self.paper_id_var.set("Select...")
		paper_id=OptionMenu(input_frame,self.paper_id_var,*paper_id_list,command=self.changeState)
		paper_id.place(x=30,y=30)


		lblc = Label(input_frame, text = "Paper Name*",font=("Time 9 bold"))
		lblc.place(x =300,y=10)
		self.paper_name=Label(input_frame,text="None",bd=2,width=18,relief=GROOVE,bg="white",font=("time 9 bold"))
		self.paper_name.place(x=300,y=30)
		
		

		
		lbl = Label(input_frame, text = "Q. No.*",font=("Time 9 bold"))
		lbl.place(x =30,y=70)
		
		qno = Entry(input_frame,textvariable=self.question_no,width =5,relief=GROOVE,bd=2,font=("Time 9 bold"))
		qno.place(x=80,y=70)
		
		lbl1 = Label(input_frame, text = "Question*",font=("Time 9 bold"))
		lbl1.place(x =30,y=100)
		self.question = Text(input_frame, width =60,height=5,relief=GROOVE,bd=2)
		self.question.place(x =30,y=120)
		lbl2 = Label(input_frame, text = "Option1 *",font=("Time 9 bold"))
		lbl2.place(x =30,y=230)
		Option1 = Entry(input_frame,textvariable=self.option1, width = 65,relief=GROOVE,bd=2)
		Option1.place(x =30,y=250)

		lbl3 = Label(input_frame, text = "Option2*",font=("Time 9 bold"))
		lbl3.place(x =30,y=280)
		option2 = Entry(input_frame,textvariable=self.option2, width = 65,relief=GROOVE,bd=2)
		option2.place(x =30,y=300)

		lbl4 = Label(input_frame, text = "Option3*",font=("Time 9 bold"))
		lbl4.place(x =30,y=330)
		option3 = Entry(input_frame,textvariable=self.option3, width = 65,relief=GROOVE,bd=2)
		option3.place(x =30,y=350)

		lbl5 = Label(input_frame, text = "Option4*",font=("Time 9 bold"))
		lbl5.place(x =30,y=380)
		option4 = Entry(input_frame,textvariable=self.option4, width = 65,relief=GROOVE,bd=2)
		option4.place(x =30,y=400)

		lbl5 = Label(input_frame, text = "Answer*",font=("Time 9 bold"))
		lbl5.place(x =30,y=430)
		answer = Entry(input_frame,textvariable=self.answer, width = 65,relief=GROOVE,bd=2)
		answer.place(x =30,y=450)

		btnadd = Button (input_frame, text = "Add",command=self.addQuestion, width = 8,background = "blue", foreground= "white",font=("Time 11 bold"))
		btnadd.place(x=25,y=515)

		btnopen=Button(input_frame,text="Open",command=self.openQuestion,width=8,bg="blue",fg="white",font=("Time 11 bold"))
		btnopen.place(x=120,y=515)


		btnupdate = Button (input_frame, text = "Update",command=self.updateQuestion, width = 8, background = "green", foreground= "white",font=("Time 11 bold"))
		btnupdate.place(x=215,y=515)

		btndelete = Button (input_frame, text = "Delete", command=self.deleteQuestion,width = 8,background = "green", foreground= "white",font=("Time 11 bold"))
		btndelete.place(x=310,y=515)

		btnclear = Button (input_frame, text = "Clear",command=self.clearEntry, width =8,background = "red", foreground= "white",font=("Time 11 bold"))
		btnclear.place(x=405,y=515)


		window.mainloop()
	def changeState(self,item):
		self.run()
		if item=="Select":
			pass

		else:
			
			sql="select paper_name from ExamDashboard where paper_id=%s"
			self.mycursor.execute(sql,[item,]) 
			paper_name=self.mycursor.fetchone()
			self.paper_name.config(text=paper_name[0])

			sql2="select count(*) from "+item
			self.mycursor.execute(sql2)
			max_row=self.mycursor.fetchall()
			self.question_no.set(max_row[0][0])
			#print(max_row[0][0])
			
	def addQuestion(self):
		self.run()
		try:
			sql="insert into "+self.paper_id_var.get() +"(qno,question,option1,option2,option3,option4,answer,submit_date) values(%s,%s,%s,%s,%s,%s,%s,CURDATE())"
			self.mycursor.execute(sql,[self.question_no.get(),self.question.get("1.0",END),self.option1.get(),self.option2.get(),self.option3.get(),self.option4.get(),self.answer.get()])
			self.mydb.commit()# it make database modifiable
			messagebox.showinfo("Status","Successfully Added ")
			self.clearEntry()
			qno=int(self.question_no.get())+1
			self.question_no.set(qno)
		except:
			messagebox.showwarning("Error","Try again!!. Can't be added")
	def openQuestion(self):
		self.run()
		try:
			self.question.delete("1.0",END)	
			if int(self.question_no.get()==None):
				messagebox.showinfo("Please enter Question No.")
			
			sql="select * from "+self.paper_id_var.get()+" where qno=%s"
			self.mycursor.execute(sql,[self.question_no.get()])
			question=self.mycursor.fetchone()
				
			self.question_no.set(question[0])	
			self.question.insert(INSERT,question[1])
			self.option1.set(question[2])
			self.option2.set(question[3])
			self.option3.set(question[4])
			self.option4.set(question[5])
			self.answer.set(question[6])

		except:

			messagebox.showwarning("Not Found!","This question is not exit!!")

	def deleteQuestion(self):
		self.run()
		try:
		
			sql="delete  from "+self.paper_id_var.get()+" where qno=%s"#+self.paper_id_var.get() +
			self.mycursor.execute(sql,[int(self.question_no.get())])
			self.mydb.commit()
			self.question.delete("1.0",END)
			self.option1.set("")
			self.option2.set("")
			self.option3.set("")
			self.option4.set("")
			self.answer.set("")
		

			messagebox.showinfo("Status","Successfully deleted Question No "+self.question_no.get())

		except:
			messagebox.showwarning("Status","Try again!!\n Can't Deleted!!")

	def updateQuestion(self):
		self.run()
		try:
		
			sql="update "+self.paper_id_var.get()+" set question= %s,option1=%s,option2=%s,option3=%s,option4=%s,answer=%s where qno=%s"
			self.mycursor.execute(sql,[self.question.get("1.0",END),self.option1.get(),self.option2.get(),self.option3.get(),self.option4.get(),self.answer.get(),self.question_no.get()])
			self.mydb.commit()
			self.question.delete("1.0",END)
			self.option1.set("")
			self.option2.set("")
			self.option3.set("")
			self.option4.set("")
			self.answer.set("")
		
			messagebox.showinfo("Status","Successfully Updated Question No. "+self.question_no.get())
		except:
			messagebox.showwarning("Status","Can't be updated!!\n Try again..")

	def clearEntry(self):
		
		self.question.delete("1.0",END)
		self.option1.set("")
		self.option2.set("")
		self.option3.set("")
		self.option4.set("")
		self.answer.set("")

	def run(self):
		
		self.hostname = socket.gethostname()    
		self.IPAddr = socket.gethostbyname(self.hostname) 
		while(self.IPAddr=="127.0.0.1"):
			messagebox.showerror("","No Network Connection. Please connect to the network.")
			self.IPAddr = socket.gethostbyname(self.hostname) 
		

#obj=AddQuestion()