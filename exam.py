from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from tkinter import ttk
import mysql.connector as mysql
from tkinter import messagebox
from datetime import date

root=Tk()
width_screen=root.winfo_screenwidth()
height_screen=root.winfo_screenheight()
root.title("exam/taskninja")
root.geometry(f"{width_screen}x{height_screen}")
root.minsize("400","300")
root.state("zoomed")

def planner():
    root.destroy()
    import dailyplanner
def cal():
    root.destroy()
    import ca
def quiz():
    root.destroy()
    import quiz
def das():
    root.destroy()
    import dashboard2
def user():
    root.destroy()
    import setting 
    
def submit():
    days_in_month=31
    days_day_num=int(today.strftime("%d"))
    count= Label(root,text=f" Today is: {days_day_num} of the month",font=("Poppins", 15, "bold"))
    count.place(x=630,y=500)
    if int(days_exam.get())<=32:
        if int(days_exam.get())<days_day_num:
            day_left = days_in_month-days_day_num+int(days_exam.get())
            count1= Label(root,text=f"{day_left} days left for your Examinations",font=("Poppins", 15, "bold"))
            count1.place(x=600,y=550)
        else:
            day_left2 = int(days_exam.get())-days_day_num
            count1= Label(root,text=f"{day_left2} days left for your Examinations",font=("Poppins", 15, "bold"))
            count1.place(x=600,y=550)
    else:
        count2= Label(root,text=f"Please enter a valid Date",font=("Poppins", 15, "bold"))
        count2.place(x=630,y=550)


    

frame=Frame(width=160,padx=30,bg='black')
frame.pack(side=LEFT,fill=Y)
dash=Button(text='Dashboard',width=15,height=3,border=1,bg='#FAFAFA',fg='black',font=("Inter", 12, "bold"),cursor='hand2',command=das)
dash.place(x=1,y=30)
dailyplanner=Button(text='Daily planner',width=15,height=3,border=1,bg='#FAFAFA',fg='black',font=("Inter", 12, "bold"),cursor='hand2',command=planner)
dailyplanner.place(x=1,y=100)
calendar=Button(text='Calendar',width=15,height=3,border=0,bg='#FAFAFA',fg='black',font=("Inter", 12, "bold"),cursor='hand2',command=cal)
calendar.place(x=1,y=170)
quiz2=Button(text='Quiz',width=15,height=3,border=0,bg='#FAFAFA',fg='black',font=("Inter", 12, "bold"),cursor='hand2',command=quiz)
quiz2.place(x=1,y=240)
exam2=Button(text='Exam',width=15,height=3,border=0,bg='#FAFAFA',fg='black',font=("Inter", 12, "bold"),cursor='hand2')
exam2.place(x=1,y=310)
setting=Button(text='User Setting',width=15,height=3,border=0,bg='#FAFAFA',fg='black',font=("Inter", 12, "bold"),cursor='hand2',command=user)
setting.place(x=1,y=380)

panic=Label(root,text="DON'T PANIC !",font=("Poppins", 20, "bold"),bg="grey",border=21)
panic.pack(pady=20,ipadx=10,ipady=10)


today= date.today()
f_today=today.strftime("%A - %B %d,%Y")
today_lavel=Label(root,text=f"Today is: {f_today}",font=("Poppins", 15, "bold"))
today_lavel.pack(pady=20)

panic=Label(root,text="Enter your exam date here👇",font=("Poppins", 10, "bold"),bg="#FAFAFA")
panic.place(x=635,y=260)
days_exam=Entry(root,width=25,font=("Poppins", 12, "bold"))
days_exam.place(x=620,y=290)
Button(root,text="Submit",font=("Poppins", 15, "bold"),command=submit).place(x=700,y=320)




root.mainloop()