from tkinter import *
from tkinter import scrolledtext
import time
from PIL import Image,ImageTk
import threading
from tkinter import messagebox
import mysql.connector

class StudentExam:
	def __init__(self,ip_var,paper_id,email):
		self.paper_id=paper_id
		self.email=email
		self.sign=email+"sign"
		self.mydb = mysql.connector.connect(
		  host=ip_var,
		  user="rahul",
		  passwd="rahul123",
		  database="OnlineTest"
		)
		self.mycursor = self.mydb.cursor()
		sql="select * from QuestionSeries where paper_id=%s"		
		self.mycursor.execute(sql,[self.paper_id,])
		self.record=self.mycursor.fetchone()
		sql2="select * from StudentInfo where email=%s"
		self.mycursor.execute(sql2,[self.email,])
		self.stdn_info=self.mycursor.fetchone()
		
		self.window = Tk()
		self.window.title("Mock test")
		self.window.geometry("1200x680")
		self.window.resizable(0,0)


		self.original_stdn_pic = Image.open('stdn_img// '+self.email+'.png')
		resized_stdn_pic = self.original_stdn_pic.resize((100, 110),Image.ANTIALIAS)
		self.stdn_img = ImageTk.PhotoImage(resized_stdn_pic)

	
		self.original_stdn_sign=Image.open('stdn_img// '+self.sign+'.png')
		resized_stdn_sign=self.original_stdn_sign.resize((100, 60),Image.ANTIALIAS)
		self.stdn_sign= ImageTk.PhotoImage(resized_stdn_sign)
		top_logo=PhotoImage(file="logo//onlinemocktest.png")
		lbl = Label(self.window, text = "Online Mock Test",image=top_logo)
		lbl.place(x=115,y=0)
		img_lbl=Label(self.window,image=self.stdn_img,relief=GROOVE,bd=2)
		img_lbl.place(x=1090,y=3)

		sign_lbl=Label(self.window,image=self.stdn_sign,relief=GROOVE,bd=2).place(x=985,y=55)
		name_lbl=Label(self.window,height=4,width=28,relief=GROOVE,bd=2).place(x=985,y=117)
		stdn_name=Label(self.window,text=self.stdn_info[0]+" "+self.stdn_info[1],font=("Time 9 bold"))
		stdn_name.place(x=1030,y=129)

		paper_name=Label(self.window,text=self.record[2]+" ( "+self.record[1]+" )",font=("Time 9 "))
		paper_name.place(x=1030,y=155)
		rem_time_box=Label(self.window,height=3,width=15,relief=GROOVE,bd=2,font=("Time 9")).place(x=3,y=0)
		rem_lbl=Label(rem_time_box,text="Remainig Time",font=("Time 9 bold")).place(x=10,y=5)
		self.time_lbl=Label(rem_time_box,text="",font=("Time 13 bold"))
		self.time_lbl.place(x=13,y=25)

		note_lbl=Label(self.window,height=2,width=125,bg="white",bd=3,relief=GROOVE).place(x=10,y=55)
		note_txt=Label(note_lbl,text="Note :- Please don't press any other key like CTRL,ALT otherwise exam will ended!!",fg="red",bg="white",font=("Time 10 bold")).place(x=20,y=62)
		submit_btn=Button(self.window,text="Submit",command=self.result,font=("TIme 12 bold"),bd=2,fg="white",bg="green")
		submit_btn.place(x=900,y=57)

		chkbtn_frame1 = Frame(self.window, width = 50, height = 50, bg = "white",highlightbackground = 'black', highlightcolor = 'black', highlightthickness = 1)
		chkbtn_frame1.place(x=985,y=190)
		
		k=1
		self.b=[[0 for x in range(1,7)] for y in range(1,int(self.record[4]+1/5))] #The 2 dimensional list
		for self.i in range(int(self.record[4]/5)):
    		 for self.j in range(1,6):
    		 	self.b[self.i][self.j]=Checkbutton(chkbtn_frame1,text=k,bg="lightgrey",font=("Time 9 bold "))
    		 	
    		 	self.b[self.i][self.j].grid(row=self.i,column=self.j)
    		 	
    		 	k+=1
		
		
		#main screen for question view
		question_frame = Frame(self.window, width =965,bg="white",bd=2,relief=GROOVE, height = 495)

		question_frame.place(x=5,y=95)

		ques_ans_sql="select * from "+self.paper_id+" where qno=1"
		self.mycursor.execute(ques_ans_sql)
		ques_record=self.mycursor.fetchone()		

		
		self.qn_var=StringVar(question_frame)
		self.qn_var.set(str(ques_record[0])+")")
		qn=Label(question_frame,textvariable=self.qn_var, background = "white",bd=2,font=("Time 12 bold"))
		qn.place(x=20,y=25)

		
		

		self.question_var=StringVar(question_frame)
		self.question_var.set(ques_record[1])
		question=Label(question_frame,textvariable=self.question_var,font=("Time 12"),bg="white")
		question.place(x=40, y=25)

		
		self.radio_var=StringVar()
		self.radio_var.set("")
		
		self.op1 = Radiobutton(question_frame,text="",command=self.add_in_dict, variable=self.radio_var, value = 1, bg= "white",font=("Time 11"),tristatevalue="x")
		self.op1.place(x = 20, y= 150)


		self.op2 = Radiobutton(question_frame,text="",command=self.add_in_dict, variable= self.radio_var, value = 2, bg= "white",font=("Time 11"),tristatevalue="x")
		self.op2.place(x = 20, y= 200)

		self.op3 = Radiobutton(question_frame,text="",command=self.add_in_dict, variable= self.radio_var, value = 3, bg= "white",font=("Time 11"),tristatevalue="x")
		self.op3.place(x = 20, y= 250)

		self.op4 = Radiobutton(question_frame,text="",command=self.add_in_dict, variable= self.radio_var, value = 4, bg= "white",font=("Time 11"),tristatevalue="x")
		self.op4.place(x = 20, y= 300)
		
		self.op1.config(text=ques_record[2])
		self.op2.config(text=ques_record[3])
		self.op3.config(text=ques_record[4])
		self.op4.config(text=ques_record[5])
		
		
		next_btn=Button(self.window,text="Save & Next",command=self.next_ques,bg="blue",fg="white",font=("time 12 bold")).place(x=630,y=593)
		clr_btn=Button(self.window,text="Clear Response ",command=self.clear_response,bg="blue",fg="white",font=("time 12 bold")).place(x=745,y=593)
		back_btn=Button(self.window,text="Back",command=self.back_ques,font=("time 12 bold"),bg="#004C99",fg="white").place(x=895,y=593)
		footer_lbl=Label(self.window,height=3,width=138,relief=GROOVE,bd=2,bg="white").place(x=0,y=630)
		ans_box=Label(self.window,height=1,width=3,bg="green").place(x=10,y=645)
		ans_lbl=Label(self.window,text="Answered",font=("Time 12"),bg="white").place(x=40,y=645)
		unans_box=Label(self.window,height=1,width=3,bg="red").place(x=140,y=645)
		unans_lbl=Label(self.window,text="Not Answered",font=("Time 12"),bg="white").place(x=170,y=645)
		not_visit_box=Label(self.window,height=1,width=3,bg="#808080").place(x=310,y=645)
		not_visit_lbl=Label(self.window,text="Not Visited",font=("Time 12"),bg="white").place(x=340,y=645)
		

		thread = threading.Thread(target=self.run, args=())
		thread.daemon = True# Daemonize thread
		thread.start()                                  # Start the execution
				
		
		self.question_dict={} # dictionary for question _no and selected answer
		self.question_ans_dict={}
		qn_ans_sql="select qno,answer from "+self.paper_id+""
		self.mycursor.execute(qn_ans_sql)
		record_an_ans=self.mycursor.fetchall()
		self.b[0][1].config(bg="red")
		for row in record_an_ans:
			
			self.question_ans_dict[row[0]]=row[1]
		

		self.window.mainloop()
		
		
	
	
	def next_ques(self):
		# For Question Option
		row_count_sql="select count(*) from "+self.paper_id+""
		self.mycursor.execute(row_count_sql)
		max_row=self.mycursor.fetchone()[0]
		
		qno=int(re.search(r'\d+',self.qn_var.get())[0])
		qno+=1
		qn=qno
		
		if (qno<= max_row):
			ques_ans_sql="select * from "+self.paper_id+" where qno=%s"
			self.mycursor.execute(ques_ans_sql,[qno,])
			ques_record=self.mycursor.fetchall()
			
			self.qn_var.set(str(ques_record[0][0])+")")
			self.question_var.set(ques_record[0][1])
			self.op1.config(text=ques_record[0][2])
			self.op2.config(text=ques_record[0][3])
			self.op3.config(text=ques_record[0][4])
			self.op4.config(text=ques_record[0][5])
			if qno in self.question_dict:
				ans=int(self.question_dict[qno])
				if ans==1:
					self.op1.select()
				elif ans==2:
					self.op2.select()
				elif ans==3:
					self.op3.select()
				elif ans==4:
					self.op4.select()
				else:
					pass
			else:
				self.op1.deselect()
				self.op2.deselect()
				self.op3.deselect()
				self.op4.deselect()
				if qn<=5:
					self.b[0][qn].config(bg="red")
				elif qn<=10:
					qn-=5
					self.b[1][qn].config(bg="red")
				elif qn<=15:
					qn-=10
					self.b[2][qn].config(bg="red")
				elif qn<=20:
					qn-=15
					self.b[3][qn].config(bg="red")
				elif qn<=25:
					qn-=20
					self.b[4][qn].config(bg="red")
				elif qn<=30:
					qn-=25			
					self.b[5][qn].config(bg="red")
				elif qn<=35:
					qn-=30
					self.b[6][qn].config(bg="red")
				elif qn<=40:
					qn-=35
					self.b[6][qn].config(bg="red")
					
				elif qn<=45:
					qn-=40
					self.b[6][qn].config(bg="red")
				elif qn<=50:
					qn-=45
					self.b[6][qn].config(bg="red")
					
				elif qn<=55:
					qn-=50
					self.b[6][qn].config(bg="red")
					
				elif qn<=60:
					qn-=55
					self.b[6][qn].config(bg="red")
					
				elif qn<=65:
					qn-=60
					self.b[6][qn].config(bg="red")
				elif qn<=70:
					qn-=65
					self.b[6][qn].config(bg="red")
					
				elif qn<=75:
					qn-=70
					self.b[6][qn].config(bg="red")
					
				elif qn<=80:
					qn-=75
					self.b[6][qn].config(bg="red")
					
				elif qn<=85:
					qn-=80
					self.b[6][qn].config(bg="red")
				elif qn<=90:
					qn-=85
					self.b[6][qn].config(bg="red")
					
				elif qn<=95:
					qn-=90
					self.b[6][qn].config(bg="red")
					
				elif qn<=100:
					qn-=90
					self.b[6][qn].config(bg="red")
					
				elif qn<=105:
					qn-=100
					self.b[6][qn].config(bg="red")
		else:
			messagebox.showinfo("","Question Over")
			
	def back_ques(self):
		
		qno=int(re.search(r'\d+',self.qn_var.get())[0])
		qno-=1
		
		if (qno>= 1):

			ques_ans_sql="select * from "+self.paper_id+" where qno=%s"
			self.mycursor.execute(ques_ans_sql,[qno,])
			ques_record=self.mycursor.fetchall()

			self.qn_var.set(str(ques_record[0][0])+")")
			self.question_var.set(ques_record[0][1])
			self.op1.config(text=ques_record[0][2])
			self.op2.config(text=ques_record[0][3])
			self.op3.config(text=ques_record[0][4])
			self.op4.config(text=ques_record[0][5])
			
			if qno in self.question_dict:
				ans=int(self.question_dict[qno])
				if ans==1:
					self.op1.select()
				elif ans==2:
					self.op2.select()
				elif ans==3:
					self.op3.select()
				elif ans==4:
					self.op4.select()
				else:
					pass
			else:
				self.op1.deselect()
				self.op2.deselect()
				self.op3.deselect()
				self.op4.deselect()
					
		else:
			messagebox.showinfo("","No more back!!")
			
		
	def clear_response(self):
		qn=int(re.search(r'\d+',self.qn_var.get())[0])
		if qn in self.question_dict:
			self.question_dict.pop(qn)
		
		self.op1.deselect()
		self.op2.deselect()
		self.op3.deselect()
		self.op4.deselect()
		if qn<=5:
			self.b[0][qn].deselect()
			self.b[0][qn].config(bg="red")
		elif qn<=10:
			qn-=5
			self.b[1][qn].deselect()
			self.b[1][qn].config(bg="red")
		elif qn<=15:
			qn-=10
			self.b[2][qn].deselect()
			self.b[2][qn].config(bg="red")
		elif qn<=20:
			qn-=15
			self.b[3][qn].deselect()
			self.b[3][qn].config(bg="red")
		elif qn<=25:
			qn-=20
			self.b[4][qn].deselect()
			self.b[4][qn].config(bg="red")
		elif qn<=30:
			qn-=25			
			self.b[5][qn].deselect()
			self.b[5][qn].config(bg="red")
		elif qn<=35:
			qn-=30
			self.b[6][qn].deselect()
			self.b[6][qn].config(bg="red")
		elif qn<=40:
			qn-=35
			self.b[6][qn].deselect()
			self.b[6][qn].config(bg="red")
			
		elif qn<=45:
			qn-=40
			self.b[6][qn].deselect()
			self.b[6][qn].config(bg="red")
		elif qn<=50:
			qn-=45
			self.b[6][qn].deselect()
			self.b[6][qn].config(bg="red")
			
		elif qn<=55:
			qn-=50
			self.b[6][qn].deselect()
			self.b[6][qn].config(bg="red")
			
		elif qn<=60:
			qn-=55
			self.b[6][qn].deselect()
			self.b[6][qn].config(bg="red")
			
		elif qn<=65:
			qn-=60
			self.b[6][qn].deselect()
			self.b[6][qn].config(bg="red")
		elif qn<=70:
			qn-=65
			self.b[6][qn].deselect()
			self.b[6][qn].config(bg="red")
			
		elif qn<=75:
			qn-=70
			self.b[6][qn].deselect()
			self.b[6][qn].config(bg="red")
			
		elif qn<=80:
			qn-=75
			self.b[6][qn].deselect()
			self.b[6][qn].config(bg="red")
			
		elif qn<=85:
			qn-=80
			self.b[6][qn].deselect()
			self.b[6][qn].config(bg="red")
		elif qn<=90:
			qn-=85
			self.b[6][qn].deselect()
			self.b[6][qn].config(bg="red")
			
		elif qn<=95:
			qn-=90
			self.b[6][qn].deselect()
			self.b[6][qn].config(bg="red")
			
		elif qn<=100:
			qn-=90
			self.b[6][qn].deselect()
			self.b[6][qn].config(bg="red")
			
		elif qn<=105:
			qn-=100
			self.b[6][qn].deselect()
			self.b[6][qn].config(bg="red")
		

	def add_in_dict(self):
		qn=int(re.search(r'\d+',self.qn_var.get())[0])
		if qn in self.question_dict:
			self.question_dict[qn]=self.radio_var.get()
		else:
			self.question_dict[qn]=self.radio_var.get()

		if qn<=5:
			self.b[0][qn].select()
			self.b[0][qn].config(bg="green")
		elif qn<=10:
			qn-=5
			self.b[1][qn].select()
			self.b[1][qn].config(bg="green")
		elif qn<=15:
			qn-=10
			self.b[2][qn].select()
			self.b[2][qn].config(bg="green")
		elif qn<=20:
			qn-=15
			self.b[3][qn].select()
			self.b[3][qn].config(bg="green")
		elif qn<=25:
			qn-=20
			self.b[4][qn].select()
			self.b[4][qn].config(bg="green")
		elif qn<=30:
			qn-=25			
			self.b[5][qn].select()
			self.b[5][qn].config(bg="green")
		elif qn<=35:
			qn-=30
			self.b[6][qn].select()
			self.b[6][qn].config(bg="green")
		elif qn<=40:
			qn-=35
			self.b[6][qn].select()
			self.b[6][qn].config(bg="green")
			
		elif qn<=45:
			qn-=40
			self.b[6][qn].select()
			self.b[6][qn].config(bg="green")
		elif qn<=50:
			qn-=45
			self.b[6][qn].select()
			self.b[6][qn].config(bg="green")
			
		elif qn<=55:
			qn-=50
			self.b[6][qn].select()
			self.b[6][qn].config(bg="green")
			
		elif qn<=60:
			qn-=55
			self.b[6][qn].select()
			self.b[6][qn].config(bg="green")
			
		elif qn<=65:
			qn-=60
			self.b[6][qn].select()
			self.b[6][qn].config(bg="green")
		elif qn<=70:
			qn-=65
			self.b[6][qn].select()
			self.b[6][qn].config(bg="green")
			
		elif qn<=75:
			qn-=70
			self.b[6][qn].select()
			self.b[6][qn].config(bg="green")
			
		elif qn<=80:
			qn-=75
			self.b[6][qn].select()
			self.b[6][qn].config(bg="green")
			
		elif qn<=85:
			qn-=80
			self.b[6][qn].select()
			self.b[6][qn].config(bg="green")
		elif qn<=90:
			qn-=85
			self.b[6][qn].select()
			self.b[6][qn].config(bg="green")
			
		elif qn<=95:
			qn-=90
			self.b[6][qn].select()
			self.b[6][qn].config(bg="green")
			
		elif qn<=100:
			qn-=90
			self.b[6][qn].select()
			self.b[6][qn].config(bg="green")
			
		elif qn<=105:
			qn-=100
			self.b[6][qn].select()
			self.b[6][qn].config(bg="green")
			

	



	def result(self):
		right_ques={k:self.question_ans_dict[k] for k in self.question_ans_dict if k in self.question_dict and self.question_ans_dict[k]==self.question_dict[k]}
		
		wrong_ques=len(self.question_dict)-len(right_ques)
		gain_mark=len(right_ques)*int(self.record[5])-wrong_ques*int(self.record[6])
		attempted_ques=len(self.question_dict)
		not_attempt_ques=len(self.question_ans_dict)-len(self.question_dict)
		try:
			insert_sql="insert into result (stdn_email,paper_id,right_ques,wrong_ques,attempted_ques,not_attempted_ques,marks,submit_date) values(%s,%s,%s,%s,%s,%s,%s,CURDATE())"
			self.mycursor.execute(insert_sql,[self.email,self.paper_id,len(right_ques),wrong_ques,attempted_ques,not_attempt_ques,gain_mark])
			self.mydb.commit()
			messagebox.showinfo("","Thankyou for attending exam!!")
			self.window.destroy()
			import Connection
		except:
			messagebox.showerror("Error","Something wrong. Please Contact to Admin!!")
		
	def run(self):
		
		t=int(self.record[3])
		hr =int( t / 60)
		min = int(t % 60)-1
		sec=59
		while sec>=0:
			time_schedule=(str(hr).zfill(2),':',str(min).zfill(2), ':', str(sec).zfill(2))
			self.time_lbl.config(text=time_schedule)
			
			time.sleep(1)
			sec-=1
			

			if sec==0:
			    min-=1
			    sec=59
			if min==-1:
			    hr-=1
			    min=59   

			
			if hr==-1 and min ==59 and sec==59:
				self.window.destroy()
				import StudentLogin 
		
#obj=StudentExam()


