from tkinter import ttk
from tkinter import *
import mysql.connector
import socket 
from tkinter import messagebox
from PIL import Image,ImageTk
import tkinter.scrolledtext as scrolledtext
import base64
import io
import threading
import time
from tkinter import filedialog
class AdminControl():
	def __init__(self,user_id):
		self.admin_id=user_id
		self.root=Tk()
		self.root.geometry("1200x700")
		self.root.title("Online Mock Test")
		self.root.resizable(0,0)	
		self.hostname = socket.gethostname()    
		self.IPAddr = socket.gethostbyname(self.hostname) 
		self.mydb = mysql.connector.connect(
		  host="localhost",
		  user="root",
		  passwd="rahul123",
		  database="OnlineTest"
		)
		#self.mycursor = self.mydb.cursor()
		

		frame1=Frame(self.root,bg="white",width=200,height=700).pack(side=LEFT,anchor=NE)#202020
		frame2=Frame(self.root,bg="gray",width=1200,height=65).place(x=200,y=0)
		
		# Element of frame 1
		self.original_app_logo=Image.open('logo//app_logo.png')		 
		resized_app_logo=self.original_app_logo.resize((150,120),Image.ANTIALIAS)
		self.app_logo=ImageTk.PhotoImage(resized_app_logo)
		try:
			self.original_admin_pic=Image.open('logo//'+self.admin_id+'.png')
			resized_admin_pic=self.original_admin_pic.resize((100,100),Image.ANTIALIAS)
			self.admin_pic=ImageTk.PhotoImage(resized_admin_pic)
		except:
			self.original_admin_pic=Image.open('logo//admin_img.png')
			resized_admin_pic=self.original_admin_pic.resize((100,100),Image.ANTIALIAS)
			self.admin_pic=ImageTk.PhotoImage(resized_admin_pic)
		original_edit_btn_pic=Image.open('logo//edit_btn.png')		
		resized_edit_btn_pic=original_edit_btn_pic.resize((30,20),Image.ANTIALIAS)
		self.edit_btn=ImageTk.PhotoImage(resized_edit_btn_pic)
		homeimg=PhotoImage(file="logo//homeimg.png")
		self.original_stdn_img=Image.open('logo//admin_img.png')
		resized_stdn_pic=self.original_stdn_img.resize((100,110),Image.ANTIALIAS)
		self.stdn_img=ImageTk.PhotoImage(resized_stdn_pic)
		studentimg=PhotoImage(file="logo//studentimg.png")
		examimg=PhotoImage(file="logo//examimg.png")
		resultimg=PhotoImage(file="logo//resultimg.png")
		questionimg=PhotoImage(file="logo//questionbank.png")
		testimg=PhotoImage(file="logo//testimg.png")
		helpimg=PhotoImage(file="logo//help.png")
		smsimg=PhotoImage(file="logo//smsimg.png")

		l = Label(frame1,  image=self.app_logo,bg="white").place(x=20,y=0)
		home=Button(frame1,text="Home",image = homeimg, compound=LEFT,command=self.home,bd=4,relief=GROOVE,bg="white",highlightcolor="gray" ,pady=8,width=160,font=20).place(x=2,y=140)
		student=Button(frame1,text="Student ",image=studentimg,command=self.student,compound=LEFT,bd=4,relief=GROOVE,bg="white",highlightcolor="gray",pady=8,width=160,font=20).place(x=2,y=160+50)
		exam=Button(frame1,text="Exam ",image=examimg,command=self.exam,compound=LEFT,bd=4,bg="white",highlightcolor="gray" ,relief=GROOVE,pady=8,width=160,font=20).place(x=2,y=230+50)
		result=Button(frame1,text="Result ",image=resultimg,command=self.result,compound=LEFT,bd=4,bg="white",highlightcolor="gray" ,relief=GROOVE,pady=8,width=160,font=20).place(x=2,y=300+50)
		profile=Button(frame1,text="Profile",image =smsimg,compound=LEFT,command=self.profile,bd=4,bg="white",relief=GROOVE,highlightcolor="gray" ,pady=8,width=160,font=20).place(x=2,y=420)
		#help_btn=Button(frame1,text="Help",image=helpimg,command=self.helpSupport,compound=LEFT,bd=4,bg="white",relief=GROOVE,highlightcolor="gray" ,pady=8,width=160,font=20).place(x=2,y=490)

		#Element of frame2
		top_logo=PhotoImage(file="logo//onlinemocktest.png")
		l3=Label(frame2,text="Online Mock Test",image=top_logo).place(x=203,y=0)
		logoutimg=PhotoImage(file="logo//logoutimg.png")
		logout=Button(frame2,image=logoutimg,compound=LEFT,relief=GROOVE,width=30,font=20,command=self.logout).place(x=1150,y=5)
		#Back Button
		self.backbtnimg=PhotoImage(file="logo//backbtn.png")
		#All Images
		self.totalstudent=PhotoImage(file="logo//stdn.png")
		self.totaltestseries=PhotoImage(file="logo//totalseries.png")
		self.totaltest=PhotoImage(file="logo//totaltest.png")
		self.searchcomp=PhotoImage(file="logo//searchcomp.png")
		self.studentimg=PhotoImage(file="logo//img.png")
		self.search=PhotoImage(file="logo//search.png")
		self.print=PhotoImage(file="logo//print.png")
		
		
		if self.IPAddr=="127.0.0.1":
			messagebox.showerror("","No Internet Connection. Please connect to the network.")
			
		else:
			self.home()
			self.root.mainloop()


#Frames for button of frame1
	def home(self):
		self.run()
		homeframe=Frame(self.root,bg="white",width=1000,height=700).place(x=205,y=65)
		compname=Label(homeframe,bg="#1AD45E" ,fg="white",text="Computer Name :"+self.hostname, font=("Times 12 bold"),compound='center', relief='solid',bd=1,width=32,height=1).place(x=205,y=67)
		ipaddress=Label(homeframe,bg="#1AD45E" ,fg="white",text="IP Address :"+self.IPAddr, font=("Times 12 bold"),compound='center', relief='solid',bd=1,width=32,height=1).place(x=492,y=67)
		main_lbl=Label(homeframe,height=40,width=82,bd=2,relief=GROOVE).place(x=205,y=91)
		
		connectedcomputr=Label(homeframe,text="Connected Computer",width=39,bd=2,relief=GROOVE,font=("Time 12 bold")).place(x=789,y=67)
		#Tree View
		tree=ttk.Treeview(homeframe,selectmode='browse')
		vsb = ttk.Scrollbar(homeframe,orient="vertical",command=tree.yview)
		tree.configure(yscrollcommand=vsb.set)
		s = ttk.Style()
		s.configure('Treeview', rowheight=40)
		tree.place(x =789,y=90,height=610)
		
		tree["columns"] = ("1", "2","3","4")
		tree['show'] = 'headings'
		tree.column("1", width=40, anchor='c')
		tree.column("2", width=111, anchor='c')
		tree.column("3", width=140, anchor='c')
		tree.column("4", width=100, anchor='c')
		
		tree.heading("1", text="#")
		tree.heading("2", text="Comp. Name")
		tree.heading("3", text="IP Address")
		tree.heading("4", text="Status")
		
		
		"""for i in range(1,30):
			tree.insert("",'end',i,text="L1",values=(i,"Comp1","192.168.125.91","Active"))
			i+=1"""
		vsb.place(x=1184,y=65,height=605)



		
		"""footerlabel=Label(homeframe,text="",bg="white",width=1000,height=50).place(x=205,y=651)
		terms_condition=Button(footerlabel,text="Terms & Conditions", fg="blue",bd=0).place(x=280,y=660)
		privacy_policy=Button(footerlabel,text="Privacy Policy", fg="blue",bd=0).place(x=410,y=660)
		support=Button(footerlabel,text="Support", fg="blue",bd=0).place(x=500,y=660)"""
		
	def student(self):
		self.run()
		rowx=5
		columny=277
		studentframe=Frame(self.root,width=1000,height=127,bg="white").place(x=205,y=65)
		self.search_var=StringVar(studentframe)

		taglabel=Label(studentframe,text="Student  Management ",bd=2,relief=GROOVE,font=("Time 16 bold"),width=76,bg="green",fg="white").place(x=205,y=65)
		main_lbl=Label(studentframe,height=10,width=142,bd=2,relief=GROOVE).place(x=205,y=95)
		

		self.sv=StringVar()
		self.sv.trace("w",self.search_element)

		stdn_name=Label(main_lbl,text="Student Name :",font=("Times 12 bold ")).place(x=270,y=120)
		self.stdn_entry=Entry(main_lbl,textvariable=self.sv,relief=GROOVE,bd=2,font=16,width=22)
		self.stdn_entry.place(x=380,y=120)
		
		self.addstudent=Button(main_lbl,text="Add Student",fg="white",bg="blue",font=("time 12 bold"),command=self.studentRegister)
		self.addstudent.place(x=1080,y=110)

		#print_btn=Button(main_lbl,image=self.print,text="Print",compound=LEFT,bd=2,relief=GROOVE,bg="blue",fg="white",font=("Time 10 bold")).place(x=1110,y=108)

		#Tree View
		self.tree=ttk.Treeview(self.root,selectmode='browse')
		vsb = ttk.Scrollbar(self.root,orient="vertical",command=self.tree.yview)
		self.tree.configure(yscrollcommand=vsb.set)
		s = ttk.Style()
		s.configure('Treeview', rowheight=40)
		self.tree.place(x =205, y = 145,height=554)
		self.tree["columns"] = ("1", "2","3","4","5","6","7","8","9")
		self.tree['show'] = 'headings'
		self.tree.column("1", width=40, anchor='c')
		self.tree.column("2", width=170, anchor='c')
		self.tree.column("3", width=210, anchor='c')
		self.tree.column("4", width=130, anchor='c')
		self.tree.column("5", width=104, anchor='c')
		self.tree.column("6", width=140, anchor='c')
		self.tree.column("7", width=100, anchor='c')
		self.tree.column("8", width=100, anchor='c')
		
		self.tree.heading("1", text="Sr.No")
		self.tree.heading("2", text="Name")
		self.tree.heading("3", text="Email")
		self.tree.heading("4", text="Mobile")
		self.tree.heading("5", text="Gender")
		self.tree.heading("6", text="DOB")
		self.tree.heading("7", text="District")
		self.tree.heading("8", text="Reg. Date")
		
		#Student Database

		sql="select * from studentinfo"
		
		self.mycursor.execute(sql)
		record=self.mycursor.fetchall()
		
		self.names = []  # these are just test inputs for the tree
		k=0
		for i in record:
			self.names.append(record[k][0].lower())
			k+=1
		
		self.ids = [] #creates a list to store the ids of each entry in the tree
		j=1
		for i in range(len(self.names)):
            #creates an entry in the tree for each element of the list
            #then stores the id of the tree in the self.ids list
			 self.ids.append(self.tree.insert("", "end", text=self.names[i],values=(j,record[i][0]+" "+record[i][1],record[i][2],\
			 	record[i][3],record[i][4],record[i][5],record[i][10],record[i][13])))
			 j+=1
			
		vsb.place(x=1183,y=145,height=554)
	
	def search_element(self, *args):
		self.run()
		self.selections = [] #list of ids of matching tree entries
		for i in range(len(self.names)):
            #the below if check checks if the value of the entry matches the first characters of each element
            #in the names list up to the length of the value of the entry widget
			if self.stdn_entry.get() != "" and self.stdn_entry.get().lower()== self.names[i][:len(self.stdn_entry.get())]:
				self.selections.append(self.ids[i]) #if it matches it appends the id to the selections list
			self.tree.selection_set(self.selections) #we then select every id in the list

		
	def write_file(self,data, filename):
		self.run()
	# Convert binary data to proper format and write it on Hard Disk
		with open(filename, 'wb') as file:
			file.write(data)
	def selected(self):
		self.run()
		# setting selection by id with tag (name of a patient or whatever)
		self.tree.selection_set(self.tree.tag_has(self.search_var.get()))	
		
	def exam(self):
		self.run()
		sql="select count(*) from studentinfo"
		self.mycursor.execute(sql)
		max_stdn=self.mycursor.fetchall()
		
		sql2="select count(*) from QuestionSeries"
		self.mycursor.execute(sql2)
		max_series=self.mycursor.fetchall()

		sql3="select count(*) from ExamDashboard"
		self.mycursor.execute(sql3)
		max_test=self.mycursor.fetchall()



		rowx=207
		coly=135
		examframe=Frame(self.root,width=1000,height=700).place(x=205,y=65)
		self.paper_id=StringVar(examframe)		
		self.paper_name=StringVar(examframe)
		

		taglabel=Button(examframe,text="Dashboard",bd=0,command=self.exam).place(x=rowx,y=80)
		total_student=Label(examframe,image=self.totalstudent,text=str(max_stdn[0][0]).zfill(2),compound=CENTER,relief=GROOVE,font=("Time 25 bold"),bg="white",fg="#000066")
		total_student.place(x=rowx,y=coly)

		test_series=Label(examframe,image=self.totaltestseries,text=str(max_series[0][0]).zfill(2),compound=CENTER,relief=GROOVE,font=("Time 25 bold"),bg="white",fg="#000066")
		test_series.place(x=rowx+257,y=coly)

		total_tets=Label(examframe,image=self.totaltest,text=str(max_test[0][0]).zfill(2),compound=CENTER,relief=GROOVE,font=("Time 25 bold"),bg="white",fg="#000066")
		total_tets.place(x=rowx+517,y=coly)
		paper_id_name_lbl=Label(examframe,width=30,height=16,bd=2,relief=GROOVE).place(x=rowx+770,y=coly)
		
		box_lbl=Label(paper_id_name_lbl,text="Add Paper",font=("Time 10 bold"),bg="blue",fg="white",width=26).place(x=rowx+770,y=coly)
		add_paper_id_lbl=Label(paper_id_name_lbl,text="Paper ID*",font=("Time 9 bold")).place(x=rowx+785,y=coly+40)
		add_paper_id_entry=Entry(paper_id_name_lbl,textvariable=self.paper_id,width=25,bd=2,relief=GROOVE,font=("Time 10")).place(x=rowx+785,y=coly+60)
		
		add_paper_name_lbl=Label(paper_id_name_lbl,text="Paper Name*",font=("Time 9 bold")).place(x=rowx+785,y=coly+90)
		add_paper_name_entry=Entry(paper_id_name_lbl,textvariable=self.paper_name,width=25,bd=2,relief=GROOVE,font=("Time 10")).place(x=rowx+785,y=coly+110)
		add_paper_name_btn=Button(paper_id_name_lbl,text="Add",command=self.addPaper,bd=2,relief=GROOVE,bg="blue",fg="white",width=10,font=("Time 10")).place(x=rowx+840,y=coly+167)
		
		
		dashboaard=Button(examframe,text="Dashboard",font=("Time 12 bold"),width=16,relief=GROOVE,command=self.exam,bg="green",fg="white").place(x=rowx,y=70)
		
		qset=Button(examframe,text="Question Set",font=("Time 12 bold"),width=16,relief=GROOVE,command=self.questionSet,bg="green",fg="white").place(x=rowx+170,y=70)
		questionseries=Button(examframe,text="Question Series",font=("Time 12 bold"),width=16,relief=GROOVE,command=self.questionSeries,bg="green",fg="white").place(x=rowx+340,y=70)

		paper=Button(examframe,text="Paper",font=("Time 12 bold"),width=16,relief=GROOVE,command=self.paper,bg="green",fg="white").place(x=rowx+510,y=70)
		
		exam_setting=Button(examframe,text="Exam Setting",font=("Time 12 bold"),width=16,relief=GROOVE,command=self.examSetting,bg="green",fg="white")
		exam_setting.place(x=rowx+680,y=70)
		more_setting=Button(examframe,text="More Settings..",font=("Time 12 bold"),width=13,relief=GROOVE,command=self.moreSetting,bg="green",fg="white").place(x=rowx+850,y=70)

		exam_setting.bind("<Enter>",exam_setting.configure(activebackground="red"))
		
		"""footerlabel=Label(examframe,text="",width=1000,height=50).place(x=210,y=650)
		terms_condition=Button(footerlabel,text="Terms & Conditions", fg="blue",bd=0).place(x=280,y=660)
		privacy_policy=Button(footerlabel,text="Privacy Policy", fg="blue",bd=0).place(x=410,y=660)
		support=Button(footerlabel,text="Support", fg="blue",bd=0).place(x=500,y=660)"""


	def addPaper(self):
		self.run()
		try:
			paper_id=self.paper_id.get()
			paper_name=self.paper_name.get()
			
			sql1="select * from ExamDashboard where paper_id=%s"
			self.mycursor.execute(sql1,[paper_id])
			check_paper_id=self.mycursor.fetchone()


			if check_paper_id:

				messagebox.showwarning("Status","Paper ID already exist!!!")
			else:
				
				sql2="insert into ExamDashboard values(%s,%s)"
				self.mycursor.execute(sql2,[paper_id,paper_name])
				self.mydb.commit()#it make changes in database
				#print(paper_id,paper_name)
				
				self.mycursor.execute("show tables")
				for x in self.mycursor:
					if x==paper_id:
						print("Paper Id Already exit")

					#print(x)
				sql3="create table "+paper_id+" (qno int not null AUTO_INCREMENT PRIMARY KEY,question varchar(500),option1 varchar(300),option2 varchar(300),option3 varchar(300),option4 varchar(300),answer varchar(300),submit_date date)"
				self.mycursor.execute(sql3)
				
				
				messagebox.showinfo("Status","Successfully Added")
		except:
			messagebox.showwarning("Status","Unsuccessful,Try again !!!")





	def studentRegister(self):
		self.run()
		#self.addstudent.configure(state = DISABLED)
		
		import StudentRegister as stdn_reg
		obj=stdn_reg.StudentReg()
		del obj
		
		
		
	

	def questionSet(self):
		self.run()
		rowx=207
		coly=135
		questionset_frame=Frame(self.root,width=990,height=540,bg="white").place(x=205,y=105)
		main_lbl=Label(questionset_frame,height=39,width=140,bd=2,relief=GROOVE).place(x=210,y=108)
		taglbl=Label(questionset_frame,text="Question Set",font=("Time 10 bold"),bd=2,relief=GROOVE).place(x=220,y=105)
		#Tree View
		tree=ttk.Treeview(questionset_frame,selectmode='browse')
		vsb = ttk.Scrollbar(questionset_frame,orient="vertical",command=tree.yview)
		tree.configure(yscrollcommand=vsb.set)
		s = ttk.Style()
		s.configure('Treeview', rowheight=30)#s.configure("Treeview.Heading", font=(None, LARGE_FONT),rowheight=int(LARGE_FONT*2.5)
		tree.place(x =215, y = coly+20,height=510)
		
		tree["columns"] = ("1", "2","3","4","5","6","7","8","9","10")
		tree['show'] = 'headings'
		tree.column("1", width=40, anchor='c')
		tree.column("2", width=150, anchor='c')
		tree.column("3", width=100, anchor='c')
		tree.column("4", width=140, anchor='c')
		tree.column("5", width=80, anchor='c')
		tree.column("6", width=80, anchor='c')
		tree.column("7", width=100, anchor='c')
		tree.column("8", width=80, anchor='c')
		tree.column("9", width=100, anchor='c')
		tree.column("10", width=100, anchor='c')
		
		tree.heading("1", text="#")
		tree.heading("2", text="Title")
		tree.heading("3", text="Paper ID")
		tree.heading("4", text="Paper Name")
		tree.heading("5", text="Duration")
		tree.heading("6", text="Total\nQuestions")
		tree.heading("7", text="Question Marks")
		tree.heading("8", text="Negative\nMarking")
		tree.heading("9", text="Total Marks")
		tree.heading("10", text="Date")
		
		self.mycursor.execute("select * from QuestionSeries")
		record=self.mycursor.fetchall()
		#print(record)
		j=1
		for row in record:

			tree.insert("",'end',text="L1",values=(j,row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[9]))
			j+=1
		vsb.place(x=1180,y=coly+20,height=513)




	def questionSeries(self):
		self.run()
		sql="select * from ExamDashboard"
		self.mycursor.execute(sql)
		record=self.mycursor.fetchall()
		paper_id_list=[]
		paper_name_list=[]
		
		for row in record:
			paper_id_list.append(row[0])
			paper_name_list.append(row[1])
			#print(row[0])

		rowx=250
		coly=145
		question_frame=Frame(self.root,width=1000,height=700,bg="white").place(x=205,y=105)
		main_lbl=Label(question_frame,height=39,width=140,bd=2,relief=GROOVE).place(x=210,y=108)
		taglabel=Label(question_frame,text="Question Series",font=("Time 10 bold"),bd=2,relief=GROOVE).place(x=220,y=105)
		
		self.title_var=StringVar(question_frame)
		title=Label(question_frame,text="Title*",font=("Time 9 bold")).place(x=rowx+5,y=coly)
		title_entry=Entry(question_frame,textvariable=self.title_var,font=("Time 12"),width=50,bd=2,relief=GROOVE)
		title_entry.focus_set()
		title_entry.place(x=rowx+5,y=coly+20)
		
		paper_id_lbl=Label(question_frame,text="Paper ID*",font=("Time 9 bold")).place(x=rowx+5,y=coly+70)
		self.paper_id_var = StringVar(question_frame)
		#paper_id_entry=Entry(question_frame,textvariable=paper_id_var,width=30,bd=2,relief=GROOVE,font=("Time 12")).place(x=rowx+330,y=coly+20)
		self.paper_id_var.set("Select...") # default value
		#paper_ids={"\t\t\t\t\t\tB.Tech 1st Year\t\t\t\t\t\t","B.Tech 2nd Year","B.Tech 3rd Year","B.Tech 4th Year"}
		paper_id_menu = OptionMenu(question_frame,self.paper_id_var, *paper_id_list)
		paper_id_menu.place(x=rowx+5,y=coly+89)
		paper_id_menu.config(width=13)
		self.paper_id_var.trace("w", self.search_paper_name)		

		paper_name_lbl=Label(question_frame,text="Paper Name*",font=("Time 9 bold")).place(x=rowx+150,y=coly+70)
		self.paper_name_var=StringVar(question_frame)
		self.paper_name_var.set("None")
		paper_name=Label(question_frame,textvariable=self.paper_name_var,font=("Time 11"),fg="blue",bg="white",width=17,bd=2,relief=GROOVE)
		paper_name.place(x=rowx+147,y=coly+91)
		
		self.duration_var=IntVar(question_frame)
		duration=Label(question_frame,text="Duration*(In Minute)",font=("Time 9 bold")).place(x=rowx+330,y=coly+70)
		duration_entry=Entry(question_frame,textvariable=self.duration_var,width=30,bd=2,relief=GROOVE,font=("Time 12")).place(x=rowx+330,y=coly+90)

		self.ttlquestion_var=IntVar(question_frame)
		ttlquestion=Label(question_frame,text="Total Question*",font=("Time 9 bold")).place(x=rowx+5,y=coly+140)
		ttlquestion_entry=Entry(question_frame,textvariable=self.ttlquestion_var,font=("Time 12"),width=30,bd=2,relief=GROOVE)
		ttlquestion_entry.place(x=rowx+5,y=coly+160)
		ttlquestion_entry.bind('<FocusOut>',self.totalMarks )

		self.ques_mark_var=IntVar(question_frame)
		ques_mark_lbl=Label(question_frame,text="Question Mark* (for each question)",font=("Time 9 bold")).place(x=rowx+330,y=coly+140)
		ques_mark_entry=Entry(question_frame,textvariable=self.ques_mark_var,font=("Time 12"),width=30,bd=2,relief=GROOVE)
		ques_mark_entry.place(x=rowx+330,y=coly+160)
		
		#print(abc)
		ques_mark_entry.bind('<FocusOut>',self.totalMarks )
		
		self.negmarks_btn=StringVar(question_frame)

		self.neg_mark_var=IntVar(question_frame)
		negmarks=Label(question_frame,text="Negative Marks*",font=("Time 9 bold")).place(x=rowx+5,y=coly+210)
		negmarks_option1=Radiobutton(question_frame,text="Yes",value="YES",variable=self.negmarks_btn,command=self.neg_mark_enable)
		negmarks_option1.place(x=rowx+5,y=coly+230)
		negmarks_option2=Radiobutton(question_frame,text="No",value="NO",variable=self.negmarks_btn,command=self.neg_mark_disable)
		negmarks_option2.place(x=rowx+50,y=coly+230)
		self.neg_mark_entry=Entry(question_frame,textvariable=self.neg_mark_var,font=("Time 12" ),width=15,bd=2,relief=GROOVE)
		self.neg_mark_entry.place(x=rowx+100,y=coly+230)
		self.ttlmarks_var=IntVar(question_frame)
		
		ttlmarks=Label(question_frame,text="Total Marks*",font=("Time 9 bold")).place(x=rowx+330,y=coly+210)
		ttlmarks_entry=Entry(question_frame,textvariable=self.ttlmarks_var,font=("Time 12"),width=30,bd=2,relief=GROOVE).place(x=rowx+330,y=coly+230)
		instruction=Label(question_frame,text="Instruction for this Question Set*",font=("Time 9 bold")).place(x=rowx+5,y=coly+280)
		
		self.txt = scrolledtext.ScrolledText(question_frame,height=12,width=114,bd=2,relief=GROOVE,undo=True)
		self.txt.place(x=rowx+5,y=coly+300)
		
		notelabel=Label(question_frame,text="Instructions",font=("Time 9 bold")).place(x=rowx+640,y=coly+5)
		note=Label(question_frame,bd=2,relief=GROOVE,height=16,width=40).place(x=rowx+640,y=coly+25)
		note1=Label(note,text="1):-   Fields marked with * are mendatory",font=("Time 9")).place(x=rowx+655,y=coly+35)
		note2=Label(note,text="2):-   Add Paper ID & Paper Name in\n Dashboard Section ",font=("Time 9")).place(x=rowx+655,y=coly+55)		
		
		submit_btn=Button(question_frame,text="Submit",command=self.addQuestionSeries,bg="blue",fg="white",font=("Time 12"))
		submit_btn.place(x=rowx+370,y=coly+510)
		clr_btn=Button(question_frame,text="Clear",bg="red",fg="white",font=("Time 12")).place(x=rowx+450,y=coly+510)
	def totalMarks(self,event):
		ttl_mark=self.ttlquestion_var.get()*self.ques_mark_var.get()
		#print(ttl_mark)
		self.ttlmarks_var.set(ttl_mark)
	def search_paper_name(self,id,name,ghj):
		self.run()
		sql="select * from ExamDashboard where paper_id=%s"
		self.mycursor.execute(sql,[self.paper_id_var.get(),])
		record=self.mycursor.fetchone()
		#print(record[1])
		self.paper_name_var.set(record[1])



	def addQuestionSeries(self):
		
		self.run()
		try:
			sql="insert into questionSeries values(%s,%s,%s,%s,%s,%s,%s,%s,%s,CURDATE())"
			self.mycursor.execute(sql,[self.title_var.get(),self.paper_id_var.get(),self.paper_name_var.get(),
				self.duration_var.get(),self.ttlquestion_var.get(),self.ques_mark_var.get(),
				self.neg_mark_var.get(),self.ttlmarks_var.get(),self.txt.get("1.0","end")])
			
			self.mydb.commit()
			messagebox.showinfo("Status","Successfully Added Question Series....")
	
		except:
			messagebox.showwarning("Status","Unsuccessful, Try again!!!")


	def paper(self):
		self.run()
		rowx=250
		coly=145
		paper_frame=Frame(self.root,width=1000,height=700,bg="white").place(x=205,y=105)
		lbl=Label(paper_frame,height=7,width=140,bd=2,relief=GROOVE).place(x=210,y=108)
		taglabel=Label(paper_frame,text="Paper",font=("Time 10 bold"),width=12,bd=2,relief=GROOVE).place(x=220,y=105)
		self.addpaper=Button(paper_frame,text="Add Question",font=("Time 12 bold"),fg="white",bg="blue",command=self.addQuestion)
		self.addpaper.place(x=790,y=119)
		del_ques=Button(paper_frame,text="Delete Question",command=self.delete_ques,fg="white",bg="red",font=("Time 12 bold"))
		del_ques.place(x=920,y=119)
		del_paper=Button(paper_frame,text="Delete Paper",command=self.delete_paper,fg="white",bg="red",font=("Time 12 bold"))
		del_paper.place(x=1070,y=119)
		self.showpaper_id_var=StringVar(paper_frame)
		paper_id=Label(paper_frame,text="Paper ID :",font=("Times 12 bold ")).place(x=410,y=120)
		id_entry=Entry(paper_frame,textvariable=self.showpaper_id_var,relief=GROOVE,bd=2,font=16,width=16)
		id_entry.place(x=490,y=120)
		id_entry.focus_set()
		
		search_record=Button(paper_frame,command=self.show_paper,image=self.search,bd=0,font=("Time 10 bold"))
		search_record.place(x=639,y=119)
		#print_btn=Button(paper_frame,image=self.print,text="Print",compound=LEFT,bd=2,relief=GROOVE,bg="blue",fg="white",font=("Time 10 bold")).place(x=1120,y=115)
		
		self.paper_tree=ttk.Treeview(paper_frame,selectmode='browse')
		vsb = ttk.Scrollbar(paper_frame,orient="vertical",command=self.paper_tree.yview)
		self.paper_tree.configure(yscrollcommand=vsb.set)
		s = ttk.Style()
		s.configure('Treeview', rowheight=40)
		self.paper_tree.place(x =210, y = coly+10,height=545)
		
		self.paper_tree["columns"] = ("1", "2","3","4","5","6","7","8")
		self.paper_tree['show'] = 'headings'
		self.paper_tree.column("1", width=40, anchor='c')
		self.paper_tree.column("2", width=250, anchor='c')
		self.paper_tree.column("3", width=120, anchor='c')
		self.paper_tree.column("4", width=120, anchor='c')
		self.paper_tree.column("5", width=120, anchor='c')
		self.paper_tree.column("6", width=120, anchor='c')
		self.paper_tree.column("7", width=120, anchor='c')
		self.paper_tree.column("8", width=80, anchor='c')
		
		
		
		self.paper_tree.heading("1", text="#")
		self.paper_tree.heading("2", text="Question")
		self.paper_tree.heading("3", text="option1")
		self.paper_tree.heading("4", text="option2")
		self.paper_tree.heading("5", text="option3")
		self.paper_tree.heading("6", text="option4")
		self.paper_tree.heading("7", text="Answer")
		self.paper_tree.heading("8", text="Date")
		
		vsb.place(x=1180,y=coly+10,height=545)
		
		

	def delete_ques(self):
		try:
			res=messagebox.askquestion('Delete Questions', 'Do you really want to delete all question?')
			if res == 'yes':
				sql="delete from "+self.showpaper_id_var.get()
				self.mycursor.execute(sql)
				self.mydb.commit
				messagebox.showinfo("Success","Successfully deleted!!")
			else :
				pass
		     	
		except:
			messagebox.showwarning("Error","Try Again!!")
	def delete_paper(self):
		try:
			res=messagebox.askquestion('Delete Paper', 'Do you really want to delete Paper?')
			if res == 'yes':
				sql="drop table "+self.showpaper_id_var
				self.mycursor.execute(sql)
				self.mydb.commit
				messagebox.showinfo("Success","Successfully deleted!!")
				x = self.paper_tree.get_children()
				for item in x:
					self.paper_tree.delete(item)
			else :
				pass
		     	
		except:
			messagebox.showwarning("Error","Try Again!!")

	def show_paper(self):
		self.run()
		if self.showpaper_id_var.get()=="":
			messagebox.showwarning("Paper ID","Please enter Paper ID")
		else:
			x = self.paper_tree.get_children()
			for item in x:
				self.paper_tree.delete(item)
			try:
				sql="select *  from "+self.showpaper_id_var.get()
				self.mycursor.execute(sql)
				question_paper=self.mycursor.fetchall()
				#print(question_paper)
				i=1
				for row in question_paper :

					self.paper_tree.insert("",'end',i,text="L1",values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
					i+=1
			except:
				messagebox.showerror("Error","Paper ID doesn't exist!!")
				x = self.paper_tree.get_children()
				for item in x:
					self.paper_tree.delete(item)
	def addQuestion(self):
		self.run()
		import AddQuestion as ad
		AddQuestion_obj=ad.AddQuestion()
	def examSetting(self):
		self.run()
		rowx=205
		coly=105
		examsetting_frame=Frame(self.root,width=1000,height=700,bg="white").place(x=rowx,y=coly)
		main_lbl=Label(examsetting_frame,height=39,width=141,bd=2,relief=GROOVE).place(x=rowx,y=coly)
		taglabel=Label(main_lbl,text="Exam Setting",font=("Time 9 bold"),width=85,bd=2,relief=GROOVE).place(x=rowx+15,y=coly+12)
		setting_lbl=Label(main_lbl,height=36,width=85,bd=2,relief=GROOVE,bg="white").place(x=rowx+15,y=coly+32)
		step1_lbl=Label(main_lbl,text="Step 1 :-",font=("Time 12 bold"),bg="white").place(x=rowx+25,y=coly+38)
		step1_lbl_box=Label(main_lbl,height=9,width=82,bd=2,relief=GROOVE,bg="white").place(x=rowx+25,y=coly+58)
		

		sql="select * from QuestionSeries"
		self.mycursor.execute(sql)
		record=self.mycursor.fetchall()
		paper_id_list=[]
		paper_name_list=[]
		for row in record:
			paper_id_list.append(row[1])
			paper_name_list.append(row[2])
			

		paper_id_lbl=Label(step1_lbl_box,text="Paper ID*",font=("Time 9 bold"),bg="white").place(x=rowx+170,y=coly+78)
		
		self.paper_id_var=StringVar(step1_lbl_box)
		self.paper_id_var.set("Select...")
		paper_id_list = OptionMenu(step1_lbl_box, self.paper_id_var, *paper_id_list)#*paper_ids)
		paper_id_list.place(x=rowx+247,y=coly+76)
		paper_id_list.config(width=10)
		self.paper_id_var.trace("w",self.search_paper_exam)

		self.mycursor.execute("select * from QuestionSeries where paper_id=%s",[self.paper_id_var.get()])
		paper_name=self.mycursor.fetchone()
		
		self.paper_name=StringVar(step1_lbl_box)
		self.paper_name.set("None")
		
		paper_name_lbl=Label(step1_lbl_box,text="Paper Name :-",font=("Time 9 bold"),bg="white").place(x=rowx+170,y=coly+122)
		self.paper_name=Label(step1_lbl_box,text="None",bg="white",fg="blue",font=("Time 9 bold"))
		self.paper_name.place(x=rowx+255,y=coly+122)
		#next_btn=Button(step1_lbl_box,text="Next",command=self.change,bg="green",fg="white",bd=2,relief=GROOVE,font=("Time 10 "),width=10).place(x=rowx+220,y=coly+148)

		step2_lbl=Label(main_lbl,text="Step 2 :-",font=("Time 12 bold"),bg="white").place(x=rowx+25,y=coly+208)
		step2_lbl_box=Label(main_lbl,height=9,width=82,bd=2,relief=GROOVE,bg="white").place(x=rowx+25,y=coly+228)
		status_exam=Button(step2_lbl_box,text="Check Status",command=self.checkStatus,bg="blue",fg="white",bd=2,relief=GROOVE,font=("Time 10"),width=10)
		status_exam.place(x=rowx+220,y=coly+248)
		total_ques_lbl=Label(step2_lbl_box,text="Total Question :-",font=("Time 9 bold"),bg="white").place(x=rowx+80,y=coly+320)
		self.total_ques=Label(step2_lbl_box,text="None",font=("Time 9 bold"),bg="white",fg="blue")
		self.total_ques.place(x=rowx+190,y=coly+320)
		found_ques_lbl=Label(step2_lbl_box,text="Found Question :-",font=("Time 9 bold"),bg="white").place(x=rowx+340,y=coly+320)
		self.found_ques=Label(step2_lbl_box,text="None",font=("Time 9 bold"),bg="white",fg="blue")
		self.found_ques.place(x=rowx+450,y=coly+320)

		step3_lbl=Label(main_lbl,text="Step 3 :-",font=("Time 12 bold"),bg="white").place(x=rowx+25,y=coly+388)
		step3_lbl_box=Label(main_lbl,height=9,width=82,bd=2,relief=GROOVE,bg="white").place(x=rowx+25,y=coly+408)
		lbl1=Label(step3_lbl_box,text="1) Establish the connection at client side by entering IP Addess and Paper ID",font=("Time 10"),bg="white").place(x=rowx+35,y=coly+420)
		lbl2=Label(step3_lbl_box,text="2) Now Student can login by their Email Id and DOB.",font=("Time 10"),bg="white").place(x=rowx+35,y=coly+450)
		lbl3=Label(step3_lbl_box,text="3) Take Exam and Submit.",font=("Time 10"),bg="white").place(x=rowx+35,y=coly+480)

		
		stdn_list_lbl=Label(main_lbl,text="Student List",bd=2,relief=GROOVE,font=("Time 9 bold"),width=46).place(x=rowx+648,y=coly+10)
		
		tree=ttk.Treeview(main_lbl,selectmode='browse')
		vsb = ttk.Scrollbar(main_lbl,orient="vertical",command=tree.yview)
		tree.configure(yscrollcommand=vsb.set)
		s = ttk.Style()
		s.configure('Treeview', rowheight=40)
		tree.place(x=rowx+647,y=coly+30,height=546)
		tree["columns"] = ("1", "2","3")
		tree['show'] = 'headings'
		tree.column("1", width=30, anchor='c')
		tree.column("2", width=203, anchor='c')
		tree.column("3", width=90, anchor='c')
		tree.heading("1", text="#")
		tree.heading("2", text="Name")
		tree.heading("3", text="Status")
		"""for i in range(1,35):
			tree.insert("",'end',i,text="L1",values=(i,"Rahul Tripathi","Active"))
			i+=1"""
		vsb.place(x=1179,y=coly+30,height=546)
	def checkStatus(self):
		sql="select * from QuestionSeries where paper_id=%s"
		self.mycursor.execute(sql,[self.paper_id_var.get()])
		record=self.mycursor.fetchone()
		sql2="select count(*) from "+self.paper_id_var.get()
		self.mycursor.execute(sql2)
		total_ques=self.mycursor.fetchall()
		if int(record[4])==int(total_ques[0][0]):
			messagebox.showinfo("","Every thing is ok. Now you can start Exam!!")

							
		else:
			messagebox.showerror("Error","This paper is not complete.Please complete the paper.")
		self.total_ques.config(text=record[4])	
		self.found_ques.config(text=total_ques[0][0])
	def moreSetting(self):
		self.run()
		moresetting_frame=Frame(self.root,width=1000,height=700,bg="white").place(x=205,y=105)
		main_lbl=Label(moresetting_frame,height=39,width=140,bd=2,relief=GROOVE).place(x=210,y=108)
		taglabel=Label(main_lbl,text="More Settings",font=("Time 10 bold"),bd=2,relief=GROOVE).place(x=220,y=105)
	


	def result(self):
		self.run()

		resultframe=Frame(self.root,width=1000,height=700).place(x=205,y=65)
		coly=140
		framelabel=Label(resultframe,height=40,width=137,relief=GROOVE,bd=2).place(x=215,y=80)
		taglabel=Label(framelabel,text="Result Management",font=("Time 9 bold")).place(x=220,y=85)
		part1=Label(resultframe,bg="white",height=35,width=60,relief=GROOVE,bd=2).place(x=240,y=110)
		genereat_result=Label(part1,text="Gernerate Result",bg="white",font=("Time 9 bold")).place(x=320,y=120)
	
		sql="select * from QuestionSeries"
		self.mycursor.execute(sql)
		record=self.mycursor.fetchall()
		paper_id_list=[]
		paper_name_list=[]
		for row in record:
			paper_id_list.append(row[1])
			

		paper_id=Label(part1,text="Paper ID*",bg="white",font=("Time 9 bold")).place(x=280,y=coly+20)
		self.paper_id_var=StringVar()
		self.paper_id_var.set("Select...")
		
		
		paper_id_option=OptionMenu(resultframe,self.paper_id_var,*paper_id_list)
		paper_id_option.config(width=30)
		paper_id_option.place(x=370,y=coly+20)
		self.paper_id_var.trace("w", self.search_paper)

		paper_name_lbl=Label(part1,text="Paper Name:",bg="white",font=("Time 9 bold")).place(x=270,y=coly+70)
		self.paper_name=Label(part1,text="None",bg="white",fg="blue",font=("Time 9 bold"))
		self.paper_name.place(x=370,y=coly+70)
		
		paper_title_lbl=Label(part1,text="Paper Title:",bg="white",font=("Time 9 bold")).place(x=270,y=coly+110)
		self.paper_title=Label(part1,text="None",bg="white",fg="blue",font=("Time 9 bold"))
		self.paper_title.place(x=370,y=coly+110)

		
		total_time_lbl=Label(part1,text="Total Time:",font=("Time 9 bold"),bg="white").place(x=270,y=coly+150)
		self.total_time=Label(part1,text="None",font=("Time 9 bold"),fg="blue",bg="white")
		self.total_time.place(x=370,y=coly+150)
		total_ques_lbl=Label(part1,text="Total Question:",font=("Time 9 bold"),bg="white").place(x=270,y=coly+190)
		self.total_ques=Label(part1,text="None",font=("Time 9 bold"),fg="blue",bg="white")
		self.total_ques.place(x=370,y=coly+190)
		
		ques_mark_lbl=Label(part1,text="Question Mark*",font=("Time 9 bold"),bg="white").place(x=270,y=coly+230)
		self.ques_mark=Label(part1,text="None",font=("time 9 bold"),fg="blue",bg="white")
		self.ques_mark.place(x=370,y=coly+230)
		
		neg_mark_lbl=Label(part1,text="Negative Marks:",bg="white",font=("Time 9 bold"))
		neg_mark_lbl.place(x=270,y=coly+270)
		self.neg_mark=Label(part1,text="None",fg="blue",bg="white",font=("Time 9 bold"))
		self.neg_mark.place(x=370,y=coly+270)

		total_mark_lbl=Label(part1,text="Total Marks:",font=("Time 9 bold"),bg="white").place(x=270,y=coly+310)
		self.total_mark=Label(part1,text="None",font=("Time 9 bold"),fg="blue",bg="white")
		self.total_mark.place(x=370,y=coly+310)
	
		genereat_result_btn=Button(part1,text="Generate Result",bd=2,relief=GROOVE,font=("Time 9 bold"),bg="green",fg="white").place(x=380,y=coly+360)


		#Part 2
		xrow=675
		
		part2=Label(resultframe,bg="white",height=35,width=69,relief=GROOVE,bd=2).place(x=668,y=110)
		genereat_result=Label(part2,text=" Result Preview",bg="white",font=("Time 9 bold")).place(x=xrow+20,y=120)
		
		self.user_email_var=StringVar(part2)
		self.user_paper_id_var=StringVar(part2)
		user_email=Label(part2,text="Email ID*",font=("Time 9 bold"),bg="white").place(x=xrow+20,y=coly+30)
		user_email_entry=Entry(part2,textvariable=self.user_email_var,width=46,bd=2,relief=GROOVE).place(x=xrow+100,y=coly+30)
		user_paper=Label(part2,text="Paper ID*",font=("Time 9 bold"),bg="white").place(x=xrow+20,y=coly+60)
		user_paper_entry=Entry(part2,textvariable=self.user_paper_id_var,width=46,bd=2,relief=GROOVE).place(x=xrow+100,y=coly+60)


		check_result_btn=Button(part2,text="Check Result",command=self.result_preview,bd=2,relief=GROOVE,font=("Time 9 bold"),bg="green",fg="white").place(x=xrow+175,y=coly+90)


		#Part3 into part2
		part3=Label(part2,bd=2,relief=GROOVE,height=18,width=62).place(x=xrow+20,y=coly+200)
		uname_lbl=Label(part3,text="Name :-",font=("Time 9 bold")).place(x=xrow+40,y=coly+220)
		self.uname=Label(part3,text="",font=("Time 9 bold"))
		self.uname.place(x=xrow+100,y=coly+220)
		self.uimg=Label(part3,image=self.stdn_img,height=100,width=90,bd=2,relief=GROOVE,bg="white")
		self.uimg.place(x=xrow+360,y=coly+210)
		paper_id_lbl=Label(part3,text="Paper ID :-",font=("Time 9 bold")).place(x=xrow+40,y=coly+250)
		self.paper_id_result=Label(part3,text="",font=("Time 9 bold"))
		self.paper_id_result.place(x=xrow+110,y=coly+250)
		paper_name_lbl=Label(part3,text="Paper Name :-",font=("Time 9 bold")).place(x=xrow+40,y=coly+280)
		self.paper_name_result=Label(part3,text="",font=("Time 9 bold"))
		self.paper_name_result.place(x=xrow+125,y=coly+280)


		totalquestion=Label(part3,text="Total Question:-",font=("Time 9 bold")).place(x=xrow+40,y=coly+310)
		self.total_question_num=Label(part3,text="",font=("Time 9 bold"))
		self.total_question_num.place(x=xrow+140,y=coly+310)
		
		right_ques=Label(part3,text="Right Questions:-",font=("Time 9 bold")).place(x=xrow+40,y=coly+340)
		self.right_ques_num=Label(part3,text="",font=("Time 9 bold"))
		self.right_ques_num.place(x=xrow+145,y=coly+340)
		wrong_ques=Label(part3,text="Wrong Question:-",font=("Time 9 bold")).place(x=xrow+40,y=coly+370)
		self.wrong_ques_num=Label(part3,text="",font=("Time 9 bold"))
		self.wrong_ques_num.place(x=xrow+150,y=coly+370)
		

		attempt_question=Label(part3,text="Attempted Question :-",font=("Time 9 bold")).place(x=xrow+40,y=coly+400)
		self.attempt_question_num=Label(part3,text="",font=("Time 9 bold"))
		self.attempt_question_num.place(x=xrow+170,y=coly+400)
		not_attempt_ques=Label(part3,text="Not Attempted Question :-",font="Time 9 bold").place(x=xrow+40,y=coly+430)
		self.not_attempt_ques_num=Label(part3,text="",font="Time 9 bold")
		self.not_attempt_ques_num.place(x=xrow+185,y=coly+430)		

		
		total_marks=Label(part3,text="Total Mark:-",font=("Time 9 bold")).place(x=xrow+340,	y=coly+340)
		self.total_marks_num=Label(part3,text="",font=("Time 9 bold"))
		self.total_marks_num.place(x=xrow+410,y=coly+340)
		gain_mark=Label(part3,text="Gain Mark:-",font=("Time 9 bold")).place(x=xrow+340,y=coly+370)
		self.gain_mark_num=Label(part3,text="",font=("Time 9 bold"))
		self.gain_mark_num.place(x=xrow+410,y=coly+370)
		ustatus_lbl=Label(part3,text="Percent(%) :-",font=("Time 9 bold")).place(x=xrow+340,y=coly+400)
		self.ustatus=Label(part3,text="",font=("Time 9 bold"))
		self.ustatus.place(x=xrow+410,y=coly+400)


	def result_preview(self):
		
		try:

			sql="select * from result where stdn_email=%s and paper_id=%s"
			self.mycursor.execute(sql,[self.user_email_var.get(),self.user_paper_id_var.get()])
			result=self.mycursor.fetchone()
			if result:
				sql2="select * from QuestionSeries where paper_id=%s"
				self.mycursor.execute(sql2,[self.user_paper_id_var.get()])
				question_info=self.mycursor.fetchone()
				sql3="select * from studentinfo where email=%s"
				self.mycursor.execute(sql3,[self.user_email_var.get(),])
				stdn_info=self.mycursor.fetchone()
				
				stdn_img=base64.b64decode(stdn_info[9])
				file_like=bytes(stdn_img)
				stdn_name=stdn_info[2]+stdn_info[0]
				
				self.write_file(file_like,"stdn img//"+stdn_name+".png")

				
				self.uname.config(text=stdn_info[0]+" "+stdn_info[1])
				self.paper_id_result.config(text=question_info[1])
				self.paper_name_result.config(text=question_info[2])
				self.total_marks_num.config(text=question_info[7])
				self.gain_mark_num.config(text=result[4])
				self.total_question_num.config(text=question_info[4])
				self.right_ques_num.config(text=result[2])
				self.wrong_ques_num.config(text=result[3])
				self.attempt_question_num.config(text=result[5])
				self.not_attempt_ques_num.config(text=result[6])
				percent=float(result[4]*100/question_info[7])
				self.ustatus.config(text=str(round(percent,2)))
				try:
					self.original_admin_pic=Image.open('stdn img//'+stdn_name+'.png')
					resized_admin_pic=self.original_admin_pic.resize((100,100),Image.ANTIALIAS)
					self.stdn_pic=ImageTk.PhotoImage(resized_admin_pic)
				except:
					self.original_admin_pic=Image.open('logo//admin_img.png')
					resized_admin_pic=self.original_admin_pic.resize((100,100),Image.ANTIALIAS)
					self.stdn_pic=ImageTk.PhotoImage(resized_admin_pic)
					
				self.uimg.config(image=self.stdn_pic)
			else:
				messagebox.showwarning("Error","This Email_ID does not exist!!")

				self.uname.config(text="")
				self.paper_id_result.config(text="")
				self.paper_name_result.config(text="")
				self.total_marks_num.config(text="")
				self.gain_mark_num.config(text="")
				self.total_question_num.config(text="")
				self.right_ques_num.config(text="")
				self.wrong_ques_num.config(text="")
				self.attempt_question_num.config(text="")
				self.not_attempt_ques_num.config(text="")
				
				self.ustatus.config(text="")
				self.original_admin_pic=Image.open('logo//admin_img.png')
				resized_admin_pic=self.original_admin_pic.resize((100,100),Image.ANTIALIAS)
				self.default_pic=ImageTk.PhotoImage(resized_admin_pic)
				self.uimg.config(image=self.default_pic)
				

			
		except:
			messagebox.showwarning("Error","This Email_ID does not exist!!")

			self.uname.config(text="")
			self.paper_id_result.config(text="")
			self.paper_name_result.config(text="")
			self.total_marks_num.config(text="")
			self.gain_mark_num.config(text="")
			self.total_question_num.config(text="")
			self.right_ques_num.config(text="")
			self.wrong_ques_num.config(text="")
			self.attempt_question_num.config(text="")
			self.not_attempt_ques_num.config(text="")
			
			self.ustatus.config(text="")
			self.original_admin_pic=Image.open('logo//admin_img.png')
			resized_admin_pic=self.original_admin_pic.resize((100,100),Image.ANTIALIAS)
			self.default_pic=ImageTk.PhotoImage(resized_admin_pic)
			self.uimg.config(image=self.default_pic)
			
	def search_paper_exam(self,i,j,k):
		self.run()

		sql="select * from  ExamDashboard where paper_id=%s "
		self.mycursor.execute(sql,[self.paper_id_var.get(),])
		record=self.mycursor.fetchone()
		self.paper_name.config(text=record[1])
	def search_paper(self,i,j,k):
		self.run()

		sql="select * from  QuestionSeries where paper_id=%s "
		self.mycursor.execute(sql,[self.paper_id_var.get(),])
		record=self.mycursor.fetchone()
		if record:
			self.paper_name.config(text=record[2])
			self.paper_title.config(text=record[0])
			self.total_time.config(text=record[3])
			self.total_ques.config(text=record[4])
			self.ques_mark.config(text=record[5])
			self.neg_mark.config(text=record[6])
			self.total_mark.config(text=record[7])
		else:
			messagebox.showerror("Result","Question Series doesn't exist for this Paper ID")
			self.paper_name.config(text="None")
			self.paper_title.config(text="None")
			self.total_time.config(text="None")
			self.total_ques.config(text="None")
			self.ques_mark.config(text="None")
			self.neg_mark.config(text="None")
			self.total_mark.config(text="None")

	def question(self):
		self.run()
		questionframe=Frame(self.root,bg="white",width=1000,height=700).place(x=205,y=65)
	
	def profile(self):
		self.run()
		rowx=207
		coly=135
		profile_frame=Frame(self.root,width=1000,height=700).place(x=205,y=65)
		main_lbl=Label(profile_frame,height=41,width=141,bd=2,relief=GROOVE).place(x=205,y=70)
		taglbl=Label(profile_frame,text="Profile",width=10,bd=2,relief=GROOVE,compound=RIGHT,font=("Time 20 bold")).place(x=rowx+400,y=70)
		info_lbl=Label(profile_frame,height=18,width=137,bd=2,relief=GROOVE).place(x=220,y=140)
		self.admin_img_lbl=Label(info_lbl,image=self.admin_pic,height=100,width=100,bd=2,relief=GROOVE)
		self.admin_img_lbl.place(x=rowx+832,y=120)
		edit_btn=Button(info_lbl,image=self.edit_btn,command=self.openImage,bd=2,relief=GROOVE).place(x=rowx+898,y=196)
		
		#Personal Details
		persnl_lbl=Label(info_lbl,text="Personal Details",relief=GROOVE,font=("Time 12 bold")).place(x=rowx+25,y=127)
		persnl_lbl_box=Label(info_lbl,bg="white",height=15,width=95,bd=2,relief=GROOVE).place(x=rowx+100,y=coly+28)
		
		sql="select * from AdminInfo where user_id=%s"
		self.mycursor.execute(sql,[self.admin_id,])
		admin_info=self.mycursor.fetchone()
		

		#Name,email,address of the admin
		email_var1=StringVar(persnl_lbl_box)
		email_var1.set(admin_info[2])
		self.name_var2=StringVar(persnl_lbl_box)
		self.name_var2.set(admin_info[3])
		self.inst_var3=StringVar(persnl_lbl_box)
		self.inst_var3.set(admin_info[4])
		
		uid_var5=StringVar(persnl_lbl_box)
		uid_var5.set(admin_info[0])
		
		adm_name_lbl=Label(persnl_lbl_box,text="Name:-",font=("Time 9 bold"),bg="white").place(x=rowx+180,y=coly+40)
		adm_name=Entry(persnl_lbl_box,textvariable=self.name_var2,font=("Time 9 bold"),width=30,bd=2,relief=GROOVE).place(x=rowx+270,y=coly+40)
		inst_name_lbl=Label(persnl_lbl_box,text="Institute:-",font=("Time 9 bold"),bg="white").place(x=rowx+180,y=coly+80)
		inst_name=Entry(persnl_lbl_box,textvariable=self.inst_var3,font=("Time 9 bold"),width=30,bd=2,relief=GROOVE).place(x=rowx+270,y=coly+80)
		address_lbl=Label(persnl_lbl_box,text="Address:-",font=("Time 9 bold"),bg="white").place(x=rowx+180,y=coly+120)
		self.address=scrolledtext.ScrolledText(persnl_lbl_box,font=("Time 9 bold"),height=5,width=40,bd=2,relief=GROOVE,undo=True)
		self.address.place(x=rowx+270,y=coly+120)
		self.address.insert(END,""+admin_info[5])
		
		update_btn=Button(persnl_lbl_box,text="Update Info",command=self.update_info,width=20,bg="green",fg="white",font=("time 10 bold")).place(x=rowx+360,y=coly+220)
		
		#Password Setting
		info_lbl2=Label(profile_frame,height=18,width=137,bd=2,relief=GROOVE).place(x=220,y=coly+280)
		paswd_lbl=Label(info_lbl2,text="Password Setting",relief=GROOVE,font=("Time 12 bold")).place(x=rowx+25,y=coly+265)
		paswd_lbl_box=Label(info_lbl2,bg="white",height=15,width=95,bd=2,relief=GROOVE).place(x=rowx+100,y=coly+310)
		email_lbl=Label(persnl_lbl_box,text="Email:-",font=("Time 9 bold"),bg="white").place(x=rowx+180,y=coly+330)
		email_id=Entry(persnl_lbl_box,textvariable=email_var1,state='readonly',font=("Time 9 bold"),width=30,fg="blue",bd=2,relief=GROOVE).place(x=rowx+300,y=coly+330)
		adm_id_lbl=Label(paswd_lbl_box,text="User ID:-",font=("Time 9 bold"),bg="white").place(x=rowx+180,y=coly+370)
		adm_id=Entry(paswd_lbl_box,textvariable=uid_var5,font=("Time 9 bold"),state='readonly',width=30,fg="blue",bg="white",bd=2,relief=GROOVE).place(x=rowx+300,y=coly+370)
		
		self.old_paswd=StringVar(paswd_lbl_box)
		self.new_paswd=StringVar(paswd_lbl_box)
		self.retype_pswd=StringVar(paswd_lbl_box)
		
		self.change_paswd=Button(paswd_lbl_box,text="Change Password",command=self.show_paswd_lbl,font=("Time 11 bold"),bg="blue",fg="white")
		self.change_paswd.place(x=rowx+620,y=coly+315)
		self.old_paswd_lbl=Label(paswd_lbl_box,text="Old Password:-",font=("Time 9 bold"),bg="white")
		self.old_paswd_entry=Entry(paswd_lbl_box,textvariable=self.old_paswd,show="*",width=26,bd=2,relief=GROOVE,font=("Time 9 bold"))
		self.new_paswd_lbl=Label(paswd_lbl_box,text="New Password:-",font=("Time 9 bold"),bg="white")
		#self.new_paswd_lbl.place(x=rowx+180,y=coly+410)
		self.new_paswd_entry=Entry(paswd_lbl_box,textvariable=self.new_paswd,width=26,bd=2,relief=GROOVE,font=("Time 9 bold "))
		#self.new_paswd_entry.place(x=rowx+270,y=coly+410)
		self.re_paswd_lbl=Label(paswd_lbl_box,text="Retype Password:-",font=("time 9 bold"),bg="white")
		#self.re_paswd_lbl.place(x=rowx+180,y=coly+450)
		self.re_paswd_entry=Entry(paswd_lbl_box,textvariable=self.retype_pswd,width=26,bd=2,relief=GROOVE,font=("Time 9 bold"))
		#self.re_paswd_entry.place(x=rowx+270,y=coly+450)
		self.save_btn=Button(paswd_lbl_box,text="Save",font=("time 10 bold"),width=10,command=self.save_admin_paswd,bg="green",fg="white")

	
		
	def openImage(self):
		try:
			self.img_file=filedialog.askopenfilename(initialdir = "Desktop",title = "Select Image",filetypes = (("Image Files","*.png"),("All Files","*.*")))
			#print(self.img_file)
			self.original_admin_pic = Image.open(self.img_file)
			resized_admin_pic = self.original_admin_pic.resize((100, 100),Image.ANTIALIAS)
			self.admin_pic = ImageTk.PhotoImage(resized_admin_pic)
			self.admin_img_lbl.config(image=self.admin_pic)
			admin_img=self.convertToBinaryData(self.img_file)
			sql="update AdminInfo set img=%s where user_id=%s"
			self.mycursor.execute(sql,[admin_img,self.admin_id,])
			self.mydb.commit()
			
			sql2="select img from AdminInfo where user_id=%s "
			self.mycursor.execute(sql2,(self.admin_id,))
			data=self.mycursor.fetchone()
		
	

			data1=base64.b64decode(data[0])
			file_like=bytes(data1)
			self.write_file(file_like,"logo//"+self.admin_id+".png")
			messagebox.showinfo("","Successfully updated!!!")
		except:
			messagebox.showerror("Error","Try Again!!")
	def convertToBinaryData(self,filename):
	# Convert digital data to binary format 
		with open(filename, 'rb') as file:
			binaryData = file.read()
			encodestring = base64.b64encode(binaryData)

		#return binaryData
		return encodestring
			

	def show_paswd_lbl(self):
		self.run()
		rowx=207
		coly=175
		self.old_paswd_lbl.place(x=rowx+180,y=coly+370)
		self.old_paswd_entry.place(x=rowx+300,y=coly+370)
		self.new_paswd_lbl.place(x=rowx+180,y=coly+410)
		self.new_paswd_entry.place(x=rowx+300,y=coly+410)
		self.re_paswd_lbl.place(x=rowx+180,y=coly+450)
		self.re_paswd_entry.place(x=rowx+300,y=coly+450)
		self.save_btn.place(x=rowx+500,y=coly+470)
		self.change_paswd.config(state=DISABLED,bg="grey")
	def hide_paswd_lbl(self):
		self.run()
		self.old_paswd_lbl.place_forget()
		self.old_paswd_entry.place_forget()
		self.new_paswd_lbl.place_forget()
		self.new_paswd_entry.place_forget()
		self.re_paswd_lbl.place_forget()
		self.re_paswd_entry.place_forget()
		self.save_btn.place_forget()

	def save_admin_paswd(self):
		self.run()
		self.change_paswd.config(state=NORMAL,bg="blue")
		self.hide_paswd_lbl()
		
		check_paswd_sql="select user_id, paswd from AdminInfo where user_id=%s and paswd=%s"
		self.mycursor.execute(check_paswd_sql,[self.admin_id,self.old_paswd.get()])
		check=self.mycursor.fetchone()
		if check:
			if self.new_paswd.get()==self.retype_pswd.get():
				sql="update AdminInfo set paswd=%s where user_id=%s"
				self.mycursor.execute(sql,[self.retype_pswd.get(),self.admin_id])
				self.mydb.commit()
				messagebox.showinfo("","Successfully updated!!")
				self.old_paswd.set("")
				self.new_paswd.set("")
				self.retype_pswd.set("")

			else:
				messagebox.showwarning("","Password Mismatch!!")
		else:
			messagebox.showerror("Error","Wrong Password. Try Again!!")

	def update_info(self):
		
		try:
			sql="update AdminInfo set uname=%s,institute_name=%s,address=%s where user_id=%s"
			self.mycursor.execute(sql,[self.name_var2.get(),self.inst_var3.get(),self.address.get("1.0", END),self.admin_id])
			self.mydb.commit()
			messagebox.showinfo("Update","Successfully Updated!!")
		except:
			messagebox.showerror("Error","Unsuccessful. Try Again!!")
	"""def helpSupport(self):

		rowx=205
		coly=65
		helpframe=Frame(self.root,width=1000,height=700).place(x=205,y=65)
		main_lbl=Label(helpframe,height=1,width=65,text="Help & Support System",bd=2,relief=GROOVE,font=("Time 18 bold")).place(x=rowx,y=coly+5)
		help_text=scrolledtext.ScrolledText(helpframe,height=36,width=120,bd=2,relief=GROOVE,undo=True)
		help_text.place(x=rowx,y=coly+40)
		help_text.insert(INSERT, "*Some text nbhjv vghv v hv g    vghvgvdf cgdgghvbnvg  vhggff bhggh bgh v gf bjhghd sds jjkum njhh bhgghv v jhgjdddrt gyyy")
		help_text.insert(END, " ndjsagfsa  savhjav Some text")
		help_text.config(state=DISABLED)"""
		




	def normalState(self):
		self.run()
		self.mark_entry.config(state=NORMAL)
		self.marklbl_entry.config(state=DISABLED)
		self.num.config(state=DISABLED)
		self.marklbl_entry2.config(state=DISABLED)
		self.marklbl_entry3.config(state=DISABLED)
		self.num2.config(state=DISABLED)
		
		#self.root.update()
	def neg_mark_enable(self):
		self.neg_mark_entry.config(state=NORMAL)
	def neg_mark_disable(self):
		self.neg_mark_entry.config(state=DISABLED)


	def disableState(self):
		self.mark_entry.config(state=DISABLED)
		self.marklbl_entry.config(state=NORMAL)
		self.num.config(state=NORMAL)
		self.marklbl_entry2.config(state=NORMAL)
		self.marklbl_entry3.config(stat=NORMAL)
		self.num2.config(state=NORMAL)
		
	def logout(self):
		self.root.destroy()
		import AdminLogin as al
		obj=al.AdminLogin()
	


	def run(self):
		
		self.hostname = socket.gethostname()    
		self.IPAddr = socket.gethostbyname(self.hostname) 
		while(self.IPAddr=="127.0.0.1"):
			messagebox.showerror("","No Network Connection. Please connect to the network.")
			self.IPAddr = socket.gethostbyname(self.hostname) 
		self.mydb = mysql.connector.connect(
		  host="localhost",
		  user="root",
		  passwd="rahul123",
		  database="OnlineTest"
		)
		self.mycursor = self.mydb.cursor()
		

#admin_control=AdminControl()

