from tkinter import *
import sys
import mysql.connector as sql
from mysql.connector import Error
from tkinter import messagebox
from tkinter import Menu
from tkinter import ttk
import tkinter as tk
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from datetime import date
import csv

class BkgrFrame(tk.Frame):
    def __init__(self, parent, file_path, width, height):
        '''To create background frame'''
        global bkrgframe
        super(BkgrFrame, self).__init__(parent, borderwidth=0, highlightthickness=0)

        self.canvas = tk.Canvas(self, width=width, height=height)
        self.canvas.pack()

        pil_img = Image.open(file_path)
        self.img = ImageTk.PhotoImage(pil_img.resize((width, height), Image.LANCZOS))
        self.bg = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)

    def add(self, widget, x, y):
        '''To add widgets to background frame'''
        global bkrgframe,add
        canvas_window = self.canvas.create_window(x, y, anchor=tk.NW, window=widget)
        return widget
    
def logout():
    '''To logout from user part or admin part on clicking logout button'''
    global window,userwindow,adminwindow,wind
    if(wind==1):
        adminwindow.destroy()
        mainwindow()
    elif(wind==2):
        userwindow.destroy()
        mainwindow()
    elif(wind==3):
        signupwindow.destroy()
        mainwindow()
    else:
        pass

# User Part

def booking_home():
      '''To go back search window on clicking back button in Booking Window'''
      global bookingwindow
      bookingwindow.destroy()
      search_window3()

def book_clear():
    '''To clear all values from text box on clicking clear button in Booking Window'''
    global txt33,txt34,txt36,txt37,txt38
    txt33.delete(0,END)
    txt34.config(state="normal")
    txt34.delete(0,END)
    txt34.config(state="disabled")
    txt36.delete(0,END)
    txt37.delete(0,END)
    txt38.delete(0,END)
    txt39.config(state="normal")
    txt39.delete(0,END)
    txt40.config(state="normal")
    txt40.delete(0,END)
    txt41.config(state="normal")
    txt41.delete(0,END)
    txt42.config(state="normal")
    txt42.delete(0,END)
    txt43.config(state="normal")
    txt43.delete(0,END)
    txt44.config(state="normal")
    txt44.delete(0,END)
    txt45.config(state="normal")
    txt45.delete(0,END)
    txt46.config(state="normal")
    txt46.delete(0,END)
    txt47.config(state="normal")
    txt47.delete(0,END)
    txt48.config(state="normal")
    txt48.delete(0,END)
    txt49.config(state="normal")
    txt49.delete(0,END)
    txt50.config(state="normal")
    txt50.delete(0,END)

def book2():
    '''To add ticket details to mysql table tickeet on clicking book button in Booking Window'''
    global bookingwindow,uname,txt32,txt33,txt34,txt35,txt36,txt37,txt38,date1
    global psngr1,psngr2,psngr3,psngr4,psngr5,psngr6,p_age1,p_age2,p_age3,p_age4,p_age5,p_age6
    try:
        connection=sql.connect(host="localhost",user="root",passwd="root",database="WONDERAIL")
        cursor=connection.cursor()
        query="SELECT TICKET_ID FROM TICKET ORDER BY TICKET_ID DESC;"
        cursor.execute(query)
        data=cursor.fetchall()
        t_id=data[0][0]
        connection.close()
    except Error as E:
            messagebox.showinfo('Please Try Again !!!',E)
    a,b,c,d,e,f,g,h=uname,t_id+1,int(txt33.get()),date1,int(txt37.get()),txt38.get(),'',txt34.get()
    try:
        connection=sql.connect(host="localhost",user="root",passwd="root",database="WONDERAIL")
        cursor=connection.cursor()
        if int(txt36.get())==1:
            g+=psngr1
            g+='-'
            g+=p_age1
        elif int(txt36.get())==2:
            g+=(psngr1)
            g+=('-')
            g+=(p_age1)
            g+=(',')
            g+=(psngr2)
            g+=('-')
            g+=(p_age2)
        elif int(txt36.get())==3:
            g+=(psngr1)
            g+=('-')
            g+=(p_age1)
            g+=(',')
            g+=(psngr2)
            g+=('-')
            g+=(p_age2)
            g+=(',')
            g+=(psngr3)
            g+=('-')
            g+=(p_age3)
        elif int(txt36.get())==4:
            g+=(psngr1)
            g+=('-')
            g+=(p_age1)
            g+=(',')
            g+=(psngr2)
            g+=('-')
            g+=(p_age2)
            g+=(',')
            g+=(psngr3)
            g+=('-')
            g+=(p_age3)
            g+=(',')
            g+=(psngr4)
            g+=('-')
            g+=(p_age4)
        elif int(txt36.get())==5:
            g+=(psngr1)
            g+=('-')
            g+=(p_age1)
            g+=(',')
            g+=(psngr2)
            g+=('-')
            g+=(p_age2)
            g+=(',')
            g+=(psngr3)
            g+=('-')
            g+=(p_age3)
            g+=(',')
            g+=(psngr4)
            g+=('-')
            g+=(p_age4)
            g+=(',')
            g+=(psngr5)
            g+=('-')
            g+=(p_age5)
        elif int(txt36.get())==6:
            g+=(psngr1)
            g+=('-')
            g+=(p_age1)
            g+=(',')
            g+=(psngr2)
            g+=('-')
            g+=(p_age2)
            g+=(',')
            g+=(psngr3)
            g+=('-')
            g+=(p_age3)
            g+=(',')
            g+=(psngr4)
            g+=('-')
            g+=(p_age4)
            g+=(',')
            g+=(psngr5)
            g+=('-')
            g+=(p_age5)
            g+=(',')
            g+=(psngr6)
            g+=('-')
            g+=(p_age6)
        query="INSERT INTO TICKET VALUES('{}',{},{},'{}',{},'{}','{}','{}');".format(a,b,c,d,e,f,g,h)
        cursor.execute(query)
        connection.commit()
        connection.close()
        messagebox.showinfo("Reservation is Successful !!!","Your Ticket would be confirmed after payment at Railway Station.\nYour Ticket Id is '{}'.\nPlease note it for further procedures...".format(b))
        bookingwindow.destroy()
        user_window()
    except Error as E:
            messagebox.showinfo('Please Try Again !!!',E) 

def book1():
    '''To check whether all details are correctly filled on clicking book button in Booking Window'''
    global bookingwindow,txt33,txt34,txt35,txt36,txt37,txt38,txt39,txt40,txt41,txt42,txt43,txt44,txt45,txt46,txt47,txt48,txt49,txt50
    global psngr1,psngr2,psngr3,psngr4,psngr5,psngr6,p_age1,p_age2,p_age3,p_age4,p_age5,p_age6
    if not txt33.get() or not txt34.get() or not txt35.get() or not txt36.get() or not txt37.get() or not txt38.get():
        messagebox.showinfo('Some Information are not Specified !!!','Please ensure all details are filled....')
    else:
        if int(txt36.get())==1:
            if not txt39.get():
                value1=1
            else:
                value1=0
                psngr1,psngr2,psngr3,psngr4,psngr5,psngr6=txt39.get(),None,None,None,None,None

            if not txt45.get():
                value2=1
            else:
                try:
                    a=int(txt45.get())
                    value2=0
                    p_age1,p_age2,p_age3,p_age4,p_age5,p_age6=txt45.get(),None,None,None,None,None
                except ValueError:
                    messagebox.showinfo('Invalid Age !!!','Please provide a valid age...')                   
                    value2=1
                                   

        elif int(txt36.get())==2:
            if not txt39.get() or not txt40.get():
                value1=1
            else:
                value1=0
                psngr1,psngr2,psngr3,psngr4,psngr5,psngr6=txt39.get(),txt40.get(),None,None,None,None

            if not txt45.get() or not txt46.get():
                value2=1
            else:
                try:
                    a,b=int(txt45.get()),int(txt46.get()) 
                    value2=0
                    p_age1,p_age2,p_age3,p_age4,p_age5,p_age6=txt45.get(),txt46.get(),None,None,None,None
                except ValueError:
                    value2=1
                    messagebox.showinfo('Invalid Age !!!','Please provide a valid age...')
               
        elif int(txt36.get())==3:
            if not txt39.get() or not txt40.get() or not txt41.get():
                value1=1
            else:
                value1=0
                psngr1,psngr2,psngr3,psngr4,psngr5,psngr6=txt39.get(),txt40.get(),txt41.get(),None,None,None

            if not txt45.get() or not txt46.get() or not txt47.get():
                value2=1
            else:
                try:
                    a,b,c=int(txt45.get()),int(txt46.get()),int(txt47.get()) 
                    value2=0
                    p_age1,p_age2,p_age3,p_age4,p_age5,p_age6=txt45.get(),txt46.get(),txt47.get(),None,None,None
                except ValueError:
                    value2=1
                    messagebox.showinfo('Invalid Age !!!','Please provide a valid age...')

        elif int(txt36.get())==4:
            if not txt39.get() or not txt40.get() or not txt41.get() or not txt42.get():
                value1=1
            else:
                value1=0
                psngr1,psngr2,psngr3,psngr4,psngr5,psngr6=txt39.get(),txt40.get(),txt41.get(),txt42.get(),None,None

            if not txt45.get() or not txt46.get() or not txt47.get() or not txt48.get():
                value2=1
            else:
                try:
                    a,b,c,d=int(txt45.get()),int(txt46.get()),int(txt47.get()),int(txt48.get()) 
                    value2=0
                    p_age1,p_age2,p_age3,p_age4,p_age5,p_age6=txt45.get(),txt46.get(),txt47.get(),txt48.get(),None,None
                except ValueError:
                    value2=1
                    messagebox.showinfo('Invalid Age !!!','Please provide a valid age...')   

        elif int(txt36.get())==5:
            if not txt39.get() or not txt40.get() or not txt41.get() or not txt42.get() or not txt43.get():
                value1=1
            else:
                value1=0
                psngr1,psngr2,psngr3,psngr4,psngr5,psngr6=txt39.get(),txt40.get(),txt41.get(),txt42.get(),txt43.get(),None

            if not txt45.get() or not txt46.get() or not txt47.get() or not txt48.get() or not txt49.get():
                value2=1
            else:
                try:
                    a,b,c,d,e=int(txt45.get()),int(txt46.get()),int(txt47.get()),int(txt48.get()),int(txt49.get()) 
                    value2=0
                    p_age1,p_age2,p_age3,p_age4,p_age5,p_age6=txt45.get(),txt46.get(),txt47.get(),txt48.get(),txt49.get(),None
                except ValueError:
                    value2=1
                    messagebox.showinfo('Invalid Age !!!','Please provide a valid age...')
                
        elif int(txt36.get())==6:
            if not txt39.get() or not txt40.get() or not txt41.get() or not txt42.get() or not txt43.get() or not txt44.get():
                value1=1
            else:
                value1=0
                psngr1,psngr2,psngr3,psngr4,psngr5,psngr6=txt39.get(),txt40.get(),txt41.get(),txt42.get(),txt43.get(),txt44.get()

            if not txt45.get() or not txt46.get() or not txt47.get() or not txt48.get() or not txt49.get() or not txt50.get():
                value2=1
            else:
                try:
                    a,b,c,d,e,f=int(txt45.get()),int(txt46.get()),int(txt47.get()),int(txt48.get()),int(txt49.get()),int(txt50.get()) 
                    value2=0
                    p_age1,p_age2,p_age3,p_age4,p_age5,p_age6=txt45.get(),txt46.get(),txt47.get(),txt48.get(),txt49.get(),txt50.get()
                except ValueError:
                    value2=1
                    messagebox.showinfo('Invalid Age !!!','Please provide a valid age...')                

        else:
            pass
        
        if value1==0 and value2==0:
            book2()            
        else:
            if value1==1 and value2==1:
                messagebox.showinfo('Passenger Details not Specified !!!','Please ensure all details of passengers are correctly filled....')
            else:
                pass
            
def booking_train1():
    '''To display train name on clicking next button in Booking Window'''
    global bookingwindow,txt33,txt34
    a=int(txt33.get())
    try:
        connection=sql.connect(host="localhost",user="root",passwd="root",database="WONDERAIL")
        cursor=connection.cursor()
        query="SELECT TRAIN_NO FROM TRAIN;"
        cursor.execute(query)
        data=cursor.fetchall()
        for x in data:
            y=str((a,))
            z=str(x)
            if y==z:
                value=1
                break
            else:
                value=2
        if value==1:
            query="SELECT TRAIN_NAME FROM TRAIN WHERE TRAIN_NO={};".format(a)
            cursor.execute(query)
            data=cursor.fetchall()
            x=data[0][0]
            txt34.config(state="normal")
            txt34.delete(0,END)
            txt34.insert(0,x)
            txt34.config(state="disabled")
        else:
            messagebox.showinfo('Train No. not found !!!','You have specified Invalid Train number...')  
    except Error as E:
        messagebox.showinfo('Please Try Again !!!',E)    

def Booking():
    '''To create booking window'''
    global searchwindow,bookingwindow,txt33,txt34,txt35,txt36,txt37,txt38,date1,txt39,txt40,txt41,txt42,txt43,txt44,txt45,txt46,txt47,txt48,txt49,txt50
    searchwindow.destroy()
    bookingwindow=Tk()
    Image_Path='Train 8.gif'
    Width,Height=700,600

    bookingwindow.title("Train Details")
    bookingwindow.geometry('{}x{}'.format(Width,Height))
    bkrgframe=BkgrFrame(bookingwindow,Image_Path,Width,Height)
    bkrgframe.pack()
    bookingwindow.resizable(width=False,height=False)

    def Booking_display():
        '''To do specific tasks on clicking next button in booking Window'''
        global bookingwindow,txt36,txt39,txt40,txt41,txt42,txt43,txt44,txt45,txt46,txt47,txt48,txt49,txt50
        if not txt33.get():
            messagebox.showinfo('Train No. Not Specified !!!','Please specify the Train No....')
        else:
            booking_train1()
            if not txt36.get():
                messagebox.showinfo('No. of Passengers Not Specified !!!','Please specify the No. of Passengers...')  
            else:
                def Sub_Booking_display():
                    '''To display passenger details slot according to given pasenger number'''
                    global bookingwindow,txt39,txt40,txt41,txt42,txt43,txt44,txt45,txt46,txt47,txt48,txt49,txt50
                    a=int(txt36.get())
                    if a<=6:
                        if a==1:
                            txt39.config(state="normal")
                            txt39.delete(0,END)
                            txt40.config(state="normal")
                            txt40.delete(0,END)
                            txt40.config(state="disabled")
                            txt41.config(state="normal")
                            txt41.delete(0,END)
                            txt41.config(state="disabled")
                            txt42.config(state="normal")
                            txt42.delete(0,END)
                            txt42.config(state="disabled")
                            txt43.config(state="normal")
                            txt43.delete(0,END)
                            txt43.config(state="disabled")
                            txt44.config(state="normal")
                            txt44.delete(0,END)
                            txt44.config(state="disabled")

                            txt45.config(state="normal")
                            txt45.delete(0,END)
                            txt46.config(state="normal")
                            txt46.delete(0,END)
                            txt46.config(state="disabled")
                            txt47.config(state="normal")
                            txt47.delete(0,END)
                            txt47.config(state="disabled")
                            txt48.config(state="normal")
                            txt48.delete(0,END)
                            txt48.config(state="disabled")
                            txt49.config(state="normal")
                            txt49.delete(0,END)
                            txt49.config(state="disabled")
                            txt50.config(state="normal")
                            txt50.delete(0,END)
                            txt50.config(state="disabled")
                            
                        elif a==2:
                            txt39.config(state="normal")
                            txt39.delete(0,END)
                            txt40.config(state="normal")
                            txt40.delete(0,END)
                            txt41.config(state="normal")
                            txt41.delete(0,END)
                            txt41.config(state="disabled")
                            txt42.config(state="normal")
                            txt42.delete(0,END)
                            txt42.config(state="disabled")
                            txt43.config(state="normal")
                            txt43.delete(0,END)
                            txt43.config(state="disabled")
                            txt44.config(state="normal")
                            txt44.delete(0,END)
                            txt44.config(state="disabled")

                            txt45.config(state="normal")
                            txt45.delete(0,END)
                            txt46.config(state="normal")
                            txt46.delete(0,END)
                            txt47.config(state="normal")
                            txt47.delete(0,END)
                            txt47.config(state="disabled")
                            txt48.config(state="normal")
                            txt48.delete(0,END)
                            txt48.config(state="disabled")
                            txt49.config(state="normal")
                            txt49.delete(0,END)
                            txt49.config(state="disabled")
                            txt50.config(state="normal")
                            txt50.delete(0,END)
                            txt50.config(state="disabled")
 
                        elif a==3:
                            txt39.config(state="normal")
                            txt39.delete(0,END)
                            txt40.config(state="normal")
                            txt40.delete(0,END)
                            txt41.config(state="normal")
                            txt41.delete(0,END)
                            txt42.config(state="normal")
                            txt42.delete(0,END)
                            txt42.config(state="disabled")
                            txt43.config(state="normal")
                            txt43.delete(0,END)
                            txt43.config(state="disabled")
                            txt44.config(state="normal")
                            txt44.delete(0,END)
                            txt44.config(state="disabled")

                            txt45.config(state="normal")
                            txt45.delete(0,END)
                            txt46.config(state="normal")
                            txt46.delete(0,END)
                            txt47.config(state="normal")
                            txt47.delete(0,END)
                            txt48.config(state="normal")
                            txt48.delete(0,END)
                            txt48.config(state="disabled")
                            txt49.config(state="normal")
                            txt49.delete(0,END)
                            txt49.config(state="disabled")
                            txt50.config(state="normal")
                            txt50.delete(0,END)
                            txt50.config(state="disabled")
                            
                        elif a==4:
                            txt39.config(state="normal")
                            txt39.delete(0,END)
                            txt40.config(state="normal")
                            txt40.delete(0,END)
                            txt41.config(state="normal")
                            txt41.delete(0,END)
                            txt42.config(state="normal")
                            txt42.delete(0,END)
                            txt43.config(state="normal")
                            txt43.delete(0,END)
                            txt43.config(state="disabled")
                            txt44.config(state="normal")
                            txt44.delete(0,END)
                            txt44.config(state="disabled")

                            txt45.config(state="normal")
                            txt45.delete(0,END)
                            txt46.config(state="normal")
                            txt46.delete(0,END)
                            txt47.config(state="normal")
                            txt47.delete(0,END)
                            txt48.config(state="normal")
                            txt48.delete(0,END)
                            txt49.config(state="normal")
                            txt49.delete(0,END)
                            txt49.config(state="disabled")
                            txt50.config(state="normal")
                            txt50.delete(0,END)
                            txt50.config(state="disabled")
                            
                        elif a==5:
                            txt39.config(state="normal")
                            txt39.delete(0,END)
                            txt40.config(state="normal")
                            txt40.delete(0,END)
                            txt41.config(state="normal")
                            txt41.delete(0,END)
                            txt42.config(state="normal")
                            txt42.delete(0,END)
                            txt43.config(state="normal")
                            txt43.delete(0,END)
                            txt44.config(state="normal")
                            txt44.delete(0,END)
                            txt44.config(state="disabled")

                            txt45.config(state="normal")
                            txt45.delete(0,END)
                            txt46.config(state="normal")
                            txt46.delete(0,END)
                            txt47.config(state="normal")
                            txt47.delete(0,END)
                            txt48.config(state="normal")
                            txt48.delete(0,END)
                            txt49.config(state="normal")
                            txt49.delete(0,END)
                            txt50.config(state="normal")
                            txt50.delete(0,END)
                            txt50.config(state="disabled")
                            
                        elif a==6:
                            txt39.config(state="normal")
                            txt39.delete(0,END)
                            txt40.config(state="normal")
                            txt40.delete(0,END)
                            txt41.config(state="normal")
                            txt41.delete(0,END)
                            txt42.config(state="normal")
                            txt42.delete(0,END)
                            txt43.config(state="normal")
                            txt43.delete(0,END)
                            txt44.config(state="normal")
                            txt44.delete(0,END)
                            
                            txt45.config(state="normal")
                            txt45.delete(0,END)
                            txt46.config(state="normal")
                            txt46.delete(0,END)
                            txt47.config(state="normal")
                            txt47.delete(0,END)
                            txt48.config(state="normal")
                            txt48.delete(0,END)
                            txt49.config(state="normal")
                            txt49.delete(0,END)
                            txt50.config(state="normal")
                            txt50.delete(0,END)
                        else:
                            pass

                    else:
                        messagebox.showinfo('Limit Exceeded','Maximum No. of Passengers is 6 !!!') 
                Sub_Booking_display()
            
    lbl33=bkrgframe.add(tk.Label(bookingwindow, text="Train No.:",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),100,50)
    lbl34=bkrgframe.add(tk.Label(bookingwindow, text="Train Name:",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),100,75)
    lbl35=bkrgframe.add(tk.Label(bookingwindow, text="Date of Journey:",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),100,100)
    lbl36=bkrgframe.add(tk.Label(bookingwindow, text="No. of Passengers:",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),100,125)
    lbl36=bkrgframe.add(tk.Label(bookingwindow, text="Maximum No. of Passengers is 6",font=("cambria",8,'bold'),bg="dark slate gray",fg="white"),400,125)
    lbl37=bkrgframe.add(tk.Label(bookingwindow, text="Mobile No.:",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),100,150)
    lbl38=bkrgframe.add(tk.Label(bookingwindow, text="Email Id:",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),100,175)

    btn1=bkrgframe.add(tk.Button(bookingwindow, text="Next",bg="dark slate gray", font=("cambria",12,'bold'),fg="white",command=Booking_display),200,200)   
    back=bkrgframe.add(tk.Button(bookingwindow,text="Back",bg="dark slate gray",font=("Arial Narrow",12,'bold'),fg="white",command=booking_home),600,50)
    btn2=bkrgframe.add(tk.Button(bookingwindow, text="Book",bg="dark slate gray", font=("cambria",12,'bold'),fg="white",command=book1),190,550)
    btn3=bkrgframe.add(tk.Button(bookingwindow, text="Clear",bg="dark slate gray", font=("cambria",12,'bold'),fg="white",command=book_clear),250,550)   

    txt33=bkrgframe.add(tk.Entry(bookingwindow,width=15),250,50)
    txt34=bkrgframe.add(tk.Entry(bookingwindow,width=15),250,75)
    txt34.config(state="disabled")
    txt35=bkrgframe.add(tk.Entry(bookingwindow,width=15),250,100)
    txt35.insert(0,date1)
    txt35.config(state="disabled")
    txt36=bkrgframe.add(tk.Entry(bookingwindow,width=15),250,125)
    txt37=bkrgframe.add(tk.Entry(bookingwindow,width=15),250,150)
    txt38=bkrgframe.add(tk.Entry(bookingwindow,width=15),250,175)

    lbl39=bkrgframe.add(tk.Label(bookingwindow, text="Name of Passenger :",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),100,250)
    lbl40=bkrgframe.add(tk.Label(bookingwindow, text="Name of Passenger :",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),100,275)
    lbl41=bkrgframe.add(tk.Label(bookingwindow, text="Name of Passenger :",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),100,300)
    lbl42=bkrgframe.add(tk.Label(bookingwindow, text="Name of Passenger :",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),100,325)
    lbl43=bkrgframe.add(tk.Label(bookingwindow, text="Name of Passenger :",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),100,350)
    lbl44=bkrgframe.add(tk.Label(bookingwindow, text="Name of Passenger :",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),100,375)

    txt39=bkrgframe.add(tk.Entry(bookingwindow,width=15),250,250)
    txt40=bkrgframe.add(tk.Entry(bookingwindow,width=15),250,275)
    txt41=bkrgframe.add(tk.Entry(bookingwindow,width=15),250,300)
    txt42=bkrgframe.add(tk.Entry(bookingwindow,width=15),250,325)
    txt43=bkrgframe.add(tk.Entry(bookingwindow,width=15),250,350)
    txt44=bkrgframe.add(tk.Entry(bookingwindow,width=15),250,375)

    lbl45=bkrgframe.add(tk.Label(bookingwindow, text="Age :",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),400,250)
    lbl46=bkrgframe.add(tk.Label(bookingwindow, text="Age :",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),400,275)
    lbl47=bkrgframe.add(tk.Label(bookingwindow, text="Age :",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),400,300)
    lbl48=bkrgframe.add(tk.Label(bookingwindow, text="Age :",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),400,325)
    lbl49=bkrgframe.add(tk.Label(bookingwindow, text="Age :",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),400,350)
    lbl50=bkrgframe.add(tk.Label(bookingwindow, text="Age :",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),400,375)

    txt45=bkrgframe.add(tk.Entry(bookingwindow,width=5),450,250)
    txt46=bkrgframe.add(tk.Entry(bookingwindow,width=5),450,275)
    txt47=bkrgframe.add(tk.Entry(bookingwindow,width=5),450,300)
    txt48=bkrgframe.add(tk.Entry(bookingwindow,width=5),450,325)
    txt49=bkrgframe.add(tk.Entry(bookingwindow,width=5),450,350)
    txt50=bkrgframe.add(tk.Entry(bookingwindow,width=5),450,375)
    

def search_home():
    '''Function to go back to go back to user window on clicking home button in search window'''
    global searchwindow,userwindow
    searchwindow.destroy()
    user_window()
    
def search_window3():
    '''To create search window'''
    global bkrgframe,userwindow,searchwindow,clkvar,txt29,txt30,txt31,a1,a2,a3
    searchwindow=Tk()
    Image_Path='Train 7.gif'
    Width,Height=700,600

    searchwindow.title("Train Details")
    searchwindow.geometry('{}x{}'.format(Width,Height))
    bkrgframe=BkgrFrame(searchwindow,Image_Path,Width,Height)
    bkrgframe.pack()
    searchwindow.resizable(width=False,height=False)

    lbl29=bkrgframe.add(tk.Label(searchwindow, text="Train",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),100,100)
    btn=bkrgframe.add(tk.Button(searchwindow, text="Book",bg="dark slate gray", font=("cambria",12,'bold'),fg="white",command=Booking),250,550)   
    back=bkrgframe.add(tk.Button(searchwindow,text="Back",bg="dark slate gray",font=("Arial Narrow",12,'bold'),fg="white",command=search_home),600,100)
    if clkvar==1:
        try:
            connection=sql.connect(host="localhost",user="root",passwd="root",database="WONDERAIL")
            cursor=connection.cursor()
            query="SELECT * FROM TRAIN WHERE TRAIN_NO={};".format(a1)
            cursor.execute(query)
            data=cursor.fetchall()
            height = len(data)
            width = 2
            x=35
            y=150
            z=10
            for i in range(height):#Row
                for j in range(width):#Columns
                    lbl=bkrgframe.add(tk.Label(searchwindow, text=data[i][j],font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),x,y)
                    x+=50
                x-=100
                y+=20
            connection.close()
        except Error as E:
            messagebox.showinfo('Please Try Again !!!',E)    
    elif clkvar==0:
        try:
            connection=sql.connect(host="localhost",user="root",passwd="root",database="WONDERAIL")
            cursor=connection.cursor()
            query="SELECT * FROM TRAIN WHERE FROM_STATION='{}' AND TO_STATION='{}';".format(a2,a3)
            cursor.execute(query)
            data=cursor.fetchall()
            connection.close()
            height = len(data)
            width = 2
            x=35
            y=150
            z=10
            for i in range(height):#Row
                for j in range(width):#Columns
                    lbl=bkrgframe.add(tk.Label(searchwindow, text=data[i][j],font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),x,y)
                    x+=50
                x-=100
                y+=20
            connection.close()
        except Error as E:
            messagebox.showinfo('Please Try Again !!!',E)               
        searchwindow.mainloop()
    else:
        pass

def search_window2():
    '''Function to check whether all details are correctly filled on clicking search button in User window'''
    global a1,a2,a3,clkvar
    if clkvar==1:
        try:
            connection=sql.connect(host="localhost",user="root",passwd="root",database="WONDERAIL")
            cursor=connection.cursor()
            query="SELECT TRAIN_NO FROM TRAIN;"
            cursor.execute(query)
            data=cursor.fetchall()
            connection.close()
            an1=int(a1)
            for i in range(len(data)):
                if an1==data[i][0]:
                    v1=1
                    break
                else:
                    v1=0
            if v1==1:
                user=userwindow
                user.destroy()
                search_window3()
            else:
                messagebox.showinfo('Invalid Train Number','The given Train Number does not exist !!!')    
        except Error as E:
            messagebox.showinfo('Please Try Again !!!',E)      
    elif clkvar==0:
        try:
            connection=sql.connect(host="localhost",user="root",passwd="root",database="WONDERAIL")
            cursor=connection.cursor()
            query="SELECT DISTINCT FROM_STATION FROM TRAIN;"
            cursor.execute(query)
            data=cursor.fetchall()
            for i in range(len(data)):
                if a2==data[i][0]:
                    v2=1
                    break
                else:
                    v2=0
            if v2==1:
                query="SELECT DISTINCT FROM_STATION FROM TRAIN;"
                cursor.execute(query)
                data=cursor.fetchall()
                for i in range(len(data)):
                    if a3==data[i][0]:
                        v3=1
                        break
                    else:
                        v3=0
                if v3==1:
                    user=userwindow
                    user.destroy()
                    search_window3()
                else:
                    messagebox.showinfo('Invalid Station','The given To Station does not exist !!!') 
            else:
                messagebox.showinfo('Invalid Station','The given From Station does not exist !!!')
            connection.close() 
        except Error as E:
            messagebox.showinfo('Please Try Again !!!',E)  
    else:
        pass
    
def search_window1():
    '''Function to check whether all details are correctly filled on clicking Search button in User window'''
    global bkrgframe,userwindow,searchwindow,a1,a2,a3,txt32,txt29,txt30,txt31,clkvar
    if not txt32.get():
            messagebox.showinfo('Date not Specified !!!','Please specify the Date of Journey...')  
    else:
        if clkvar==1:
            if not txt29.get():
                messagebox.showinfo('Train No. not Specified !!!','Please specify the Train Number...')
            else:
                a1=txt29.get()
                a2,a3=0,0
                search_window2()
        elif clkvar==0:
            if not txt30.get() or not txt31.get():
                messagebox.showinfo('Station not Specified !!!','Please specify the station...')
            else:
                a2,a3=txt30.get(),txt31.get()
                a1=0
                search_window2()
        else:
            messagebox.showinfo('Not Selected !!!','Please select the option...')
    
def click1():
    '''To decide what to do on clicking first radiobutton,i.e.,train no. in User window'''
    global txt29,txt30,txt31,txt32,btn1,clkvar
    txt29.config(state="normal")
    txt30.delete(0,END)
    txt30.config(state="disabled")
    txt31.delete(0,END)
    txt31.config(state="disabled")
    clkvar=1

def click2():
    '''To decide what to do on clicking second radiobutton,i.e.,from and to station in User Window'''
    global txt29,txt30,txt31,txt32,btn1,clkvar
    txt29.delete(0,END)
    txt29.config(state="disabled")
    txt30.config(state="normal")
    txt31.config(state="normal")
    clkvar=0
    
def user_clear():
    '''Function to clear values from text boxes on clicking clear button in User window'''
    global txt29,txt30,txt31,txt32
    txt29.delete(0,END)
    txt30.delete(0,END)
    txt31.delete(0,END)
    txt32.delete(0,END)
    
def Date_Entry():
    '''To show calendar & to select a date o journey'''
    global userwindow,date,txt32,date1
    txt32.config(state="normal")
    txt32.delete(0,END)
    x=str(date.today())
    y=x.split('-')
    yy=int(y[0])
    mm=int(y[1])
    dd=int(y[2])
    top=tk.Toplevel(userwindow)
    def print_sel():
        global date1
        date=cal.selection_get()
        date1=str(date)
        txt32.insert(0,date)
        txt32.config(state="disabled")
        top.destroy()  
    cal=Calendar(top,font="Arial 14", selectmode='day',cursor="hand1", year=yy, month=mm, day=dd)
    cal.pack(fill="both", expand=True)
    tk.Button(top, text="Ok", command=print_sel).pack()
    
def user_window():
    '''To create user window'''
    global adminwindow,value,wind,userwindow,txt29,txt30,txt31,txt32
    userwindow = Tk()
    wind=2
    Image_Path = 'Train 6.gif'
    Width,Height=700,600

    userwindow.title("User Window")
    userwindow.geometry('{}x{}'.format(Width,Height))
    bkrgframe = BkgrFrame(userwindow,Image_Path,Width,Height)
    bkrgframe.pack()
    userwindow.resizable(width=False,height=False)

    rad1=bkrgframe.add(tk.Radiobutton(userwindow,text='',bg="navajo white", padx=0,width=0,font=("Monotype Corsiva",12,'bold'),fg="red",value=1,variable=v,command=click1),10,100)
    rad2=bkrgframe.add(tk.Radiobutton(userwindow,text='',bg="navajo white",padx=0, width=0,font=("Monotype Corsiva",12,'bold'),fg="red",value=0,variable=v,command=click2),10,200)

    rad1.select()
    
    lbl29=bkrgframe.add(tk.Label(userwindow, text="Train No.:",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),100,100)
    lbl30=bkrgframe.add(tk.Label(userwindow, text="Or",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),100,150)
    lbl31=bkrgframe.add(tk.Label(userwindow, text="From Station:",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),100,200)
    lbl32=bkrgframe.add(tk.Label(userwindow, text="To Station:",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),100,250)
    lbl33=bkrgframe.add(tk.Label(userwindow, text="Date of Journey:",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),100,300)

    txt29=bkrgframe.add(tk.Entry(userwindow,width=15),250,100)
    txt30=bkrgframe.add(tk.Entry(userwindow,width=15),250,200)
    txt31=bkrgframe.add(tk.Entry(userwindow,width=15),250,250)
    txt32=bkrgframe.add(tk.Entry(userwindow,width=15),400,300)
    txt32.config(state="disabled")
    click1()
    
    btn1=bkrgframe.add(tk.Button(userwindow, text="Choose Date",bg="dark slate gray", font=("cambria",12,'bold'),fg="white",command=Date_Entry),250,300)   
    btn2=bkrgframe.add(tk.Button(userwindow, text="Clear",bg="dark slate gray", font=("cambria",12,'bold'),fg="white",command=user_clear),270,400)
    btn3=bkrgframe.add(tk.Button(userwindow, text="Search",bg="dark slate gray", font=("cambria",12,'bold'),fg="white",command=search_window1),200,400)     
    lgot=bkrgframe.add(tk.Button(userwindow,text="Log Out",bg="dark slate gray",font=("Arial Narrow",12,'bold'),fg="white",command=logout),600,50)

#Admin Part
    
def add_home():
    '''Function to go back to admin window on clicking Home button in Add window'''
    global add_window,admin_window
    add_window.destroy()
    admin_window()
    
def add_clear():
    '''Function to clear all values from text boxes on clicking clear button in Add window'''
    global txt3,txt4,txt5,txt6,txt7,txt8
    txt3.delete(0,END)
    txt4.delete(0,END)
    txt5.delete(0,END)
    txt6.delete(0,END)
    txt7.delete(0,END)
    txt8.delete(0,END)
      
def add2():
    '''Function to add new train details into the table train on clicking add button in Add window'''
    global txt3,txt4,txt5,txt6,txt7,txt8,addwindow
    a,b,c,d,e,f=int(txt3.get()),txt4.get(),txt5.get(),txt6.get(),txt7.get(),int(txt8.get())
    try:
        connection=sql.connect(host="localhost",user="root",passwd="root",database="WONDERAIL")
        cursor=connection.cursor()
        query="INSERT INTO TRAIN VALUES({},'{}','{}','{}','{}',{});".format(a,b,c,d,e,f)
        cursor.execute(query)
        connection.commit()
        connection.close()
        messagebox.showinfo("Add Train Details","Train is Added")
        add_clear()
    except Error as E:
        messagebox.showinfo('Please Try Again !!!',E)  
      
def add1():
    '''Function to check whether all details are correctly filled on clicking add button in Add window'''
    global txt3,txt4,txt5,txt6,txt7,txt8
    if not txt3.get() or not txt4.get() or not txt5.get() or not txt6.get() or not txt7.get() or not txt8.get():
        messagebox.showinfo('Details Not Specified !!!','Please specify all the Details...')
    else:
        add2()

def add_window():
    '''Function to create add window'''
    global adminwindow,add_window,txt3,txt4,txt5,txt6,txt7,txt8
    admin=adminwindow
    admin.destroy()
    add_window = Tk()
    Image_Path='Train 5.gif'
    Width,Height=700,600

    add_window.title("Add Train")
    add_window.geometry('{}x{}'.format(Width,Height))
    bkrgframe=BkgrFrame(add_window,Image_Path,Width,Height)
    bkrgframe.pack()

    lbl3= bkrgframe.add(tk.Label(add_window, text="Train No.:",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),100,100)
    lbl4= bkrgframe.add(tk.Label(add_window, text="Train Name:",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),100,150)
    lbl5= bkrgframe.add(tk.Label(add_window, text="From Station:",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),100,200)
    lbl6= bkrgframe.add(tk.Label(add_window, text="To Station:",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),100,250)
    lbl7= bkrgframe.add(tk.Label(add_window, text="Via:",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),100,300)
    lbl8= bkrgframe.add(tk.Label(add_window, text="Total Seats:",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),100,350)
    
    txt3=bkrgframe.add(tk.Entry(add_window,width=15),250,100)
    txt4=bkrgframe.add(tk.Entry(add_window,width=15),250,150)
    txt5=bkrgframe.add(tk.Entry(add_window,width=15),250,200)
    txt6=bkrgframe.add(tk.Entry(add_window,width=15),250,250)
    txt7=bkrgframe.add(tk.Entry(add_window,width=15),250,300)
    txt8=bkrgframe.add(tk.Entry(add_window,width=15),250,350)

    btn1=bkrgframe.add(tk.Button(add_window, text="Add",bg="dark slate gray", font=("cambria",12,'bold'),fg="white",command=add1),150,400)
    btn2=bkrgframe.add(tk.Button(add_window, text="Clear",bg="dark slate gray", font=("cambria",12,'bold'),fg="white",command=add_clear),250,400)
    btn3 = bkrgframe.add(tk.Button(add_window, text="Home",bg="dark slate gray", font=("cambria",12,'bold'),fg="white",command=add_home),600,50)
    add_window.mainloop()

def update_home():
    '''Function to go back to admin wiindow on clicking Show Detail button in Update window'''
    global updatewindow,admin_window
    updatewindow.destroy()
    admin_window()

def update_clear():
    '''Function to clear all values from text boxes on clicking clear button in Update window'''
    global txt15,txt16,txt17,txt18,txt19,txt20,txt21
    txt15.delete(0,END)
    txt16.delete(0,END)
    txt17.delete(0,END)
    txt18.delete(0,END)
    txt19.delete(0,END)
    txt20.delete(0,END)
    txt21.delete(0,END)

def update_submit2():
    '''Function to update train details to mysql clicking submit button in Update window'''
    global updatewindow,admin_window,txt15,txt16,txt17,txt18,txt19,txt20,txt21
    tr=txt15.get()
    a,b,c,d,e,f=txt16.get(),txt17.get(),txt18.get(),txt19.get(),txt20.get(),txt21.get()
    try:
        connection=sql.connect(host="localhost",user="root",passwd="root",database="WONDERAIL")
        cursor=connection.cursor()
        query1="UPDATE TRAIN SET TRAIN_NAME='{}' WHERE TRAIN_NO={};".format(b,tr)
        cursor.execute(query1)
        query2="UPDATE TRAIN SET FROM_STATION='{}' WHERE TRAIN_NO={};".format(c,tr)
        cursor.execute(query2)
        query3="UPDATE TRAIN SET TO_STATION='{}' WHERE TRAIN_NO={};".format(d,tr)
        cursor.execute(query3)
        query4="UPDATE TRAIN SET VIA='{}' WHERE TRAIN_NO={};".format(e,tr)
        cursor.execute(query4)
        query5="UPDATE TRAIN SET TOTAL_SEATS='{}' WHERE TRAIN_NO={};".format(f,tr)
        cursor.execute(query5)
        query6="UPDATE TRAIN SET TRAIN_NO={} WHERE TRAIN_NO={};".format(a,tr)
        cursor.execute(query6)
        connection.commit()
        connection.close()
        messagebox.showinfo("Update Train details","Train Details are Updated")
        update_clear()
    except Error as E:
        messagebox.showinfo('Please Try Again !!!',E)    

def update_submit1():
    '''Function to check all details are filled in Update window'''
    global txt15,txt16,txt17,txt18,txt19,txt20,txt21
    if not txt15.get() or not txt16.get() or not txt17.get() or not txt18.get() or not txt19.get() or not txt20.get() or not txt21.get():
        messagebox.showinfo('Details Not Specified !!!','Please specify all the Details...')
    else:
        update_submit2()
        
def update():
    '''Function to show details of train on clicking Show Detail button in Update window'''
    global txt15,txt16,txt17,txt18,txt19,txt20,txt21,updatewindow
    if not txt15.get():
        messagebox.showinfo('Train No. not Specified !!!','Please specify the Train Number...')
    else:
        tr=txt15.get()
        try:
            connection=sql.connect(host="localhost",user="root",passwd="root",database="WONDERAIL")
            cursor=connection.cursor()
            query="SELECT * FROM TRAIN WHERE TRAIN_NO={};".format(tr)
            cursor.execute(query)
            data=cursor.fetchall()
            if len(data)==0:
                messagebox.showinfo("Train not Found","The entered Train No. does not exist !!!")
            else:
                a=data[0][0]
                b=data[0][1]
                c=data[0][2]
                d=data[0][3]
                e=data[0][4]
                f=data[0][5]
                connection.close()

            lbl16=bkrgframe.add(tk.Label(updatewindow, text="Enter Train No.:",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),100,200)
            lbl17=bkrgframe.add(tk.Label(updatewindow, text="Train Name:",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),100,250)
            lbl18=bkrgframe.add(tk.Label(updatewindow, text="From Station:",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),100,300)
            lbl19=bkrgframe.add(tk.Label(updatewindow, text="To Station:",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),100,350)
            lbl20=bkrgframe.add(tk.Label(updatewindow, text="Via:",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),100,400)
            lbl21=bkrgframe.add(tk.Label(updatewindow, text="Total Seats:",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),100,450)

            txt16=bkrgframe.add(tk.Entry(updatewindow,width=15),250,200)
            txt16.insert(0,a)
            txt17=bkrgframe.add(tk.Entry(updatewindow,width=15),250,250)
            txt17.insert(0,b)
            txt18=bkrgframe.add(tk.Entry(updatewindow,width=15),250,300)
            txt18.insert(0,c)
            txt19=bkrgframe.add(tk.Entry(updatewindow,width=15),250,350)
            txt19.insert(0,d)
            txt20=bkrgframe.add(tk.Entry(updatewindow,width=15),250,400)
            txt20.insert(0,e)
            txt21=bkrgframe.add(tk.Entry(updatewindow,width=15),250,450)
            txt21.insert(0,f)
                                    
            btn1=bkrgframe.add(tk.Button(updatewindow, text="Update",bg="dark slate gray", font=("cambria",12,'bold'),fg="white",command=update_submit1),150,500)
            btn2=bkrgframe.add(tk.Button(updatewindow, text="Clear",bg="dark slate gray", font=("cambria",12,'bold'),fg="white",command=update_clear),250,500)
        except Error as E:
            messagebox.showinfo('Please Try Again !!!',E) 
        
def update_window():
    '''To create update window'''
    global txt15,txt16,txt17,txt18,txt19,txt20,txt21,updatewindow,bkrgframe
    admin=adminwindow
    admin.destroy()
    updatewindow=Tk()
    Image_Path = 'Train 4.gif'
    Width,Height=700,600  
    updatewindow.title("Update Train Details")
    updatewindow.geometry('{}x{}'.format(Width,Height))
    bkrgframe = BkgrFrame(updatewindow,Image_Path,Width,Height)
    bkrgframe.pack()
    updatewindow.resizable(width=False,height=False)

    lbl15=bkrgframe.add(tk.Label(updatewindow, text="Enter Train No.:",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),100,100)        
    txt15=bkrgframe.add(tk.Entry(updatewindow,width=15),250,100)
    btn1=bkrgframe.add(tk.Button(updatewindow, text="Show Details",bg="dark slate gray", font=("cambria",12,'bold'),fg="white",command=update),170,150)
    btn2=bkrgframe.add(tk.Button(updatewindow, text="Home",bg="dark slate gray", font=("cambria",12,'bold'),fg="white",command=update_home),600,50)
    updatewindow.mainloop()

def delete_home():
    '''Function to go back to admin window on clicking Home button in delete window'''
    global deletewindow,admin_window
    deletewindow.destroy()
    admin_window()

def delete_clear():
    '''Function to clear filled details on clicking clear button in delete window'''
    global txt22,txt23,txt24,txt25,txt26,txt27,txt28
    txt22.delete(0,END)
    txt23.delete(0,END)
    txt24.delete(0,END)
    txt25.delete(0,END)
    txt26.delete(0,END)
    txt27.delete(0,END)
    txt28.delete(0,END)
       
def delete_submit():
    '''Function to delete train from MySQL table on clicking Delete button'''
    global txt22,deletewindow,bkrgframe,admin_window
    if not txt22.get():
        messagebox.showinfo('Train No. not Specified !!!','Please specify the Train Number...')
    else:
        tr=txt22.get()
        try:
            connection=sql.connect(host="localhost",user="root",passwd="root",database="WONDERAIL")
            cursor=connection.cursor()
            query="DELETE FROM TRAIN WHERE TRAIN_NO={};".format(tr)
            cursor.execute(query)
            connection.commit()
            connection.close()
            messagebox.showinfo("Delete Train details","Train Details are Deleted")
            delete_clear()
        except Error as E:
            messagebox.showinfo('Server Failure',E)

def delete_update():
    '''Function to show details of train on clicking Show details button in delete window'''
    global txt22,txt23,txt24,txt25,txt26,txt27,txt28,deletewindow,bkrgframe,admin_window
    if not txt22.get():
        messagebox.showinfo('Train No. not Specified !!!','Please specify the Train Number...')
    else:
        tr=txt22.get()
        try:
            connection=sql.connect(host="localhost",user="root",passwd="root",database="WONDERAIL")
            cursor=connection.cursor()
            query="SELECT * FROM TRAIN WHERE TRAIN_NO={};".format(tr)
            cursor.execute(query)
            data=cursor.fetchall()
            connection.close()
            if len(data)==0:
                messagebox.showinfo("Train not Found","The entered Train No. does not exist !!!")
            else:
                a=data[0][0]
                b=data[0][1]
                c=data[0][2]
                d=data[0][3]
                e=data[0][4]
                f=data[0][5]
            lbl23=bkrgframe.add(tk.Label(deletewindow, text="Enter Train No.:",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),100,200)
            lbl24=bkrgframe.add(tk.Label(deletewindow, text="Train Name:",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),100,250)
            lbl25=bkrgframe.add(tk.Label(deletewindow, text="From Station:",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),100,300)
            lbl26=bkrgframe.add(tk.Label(deletewindow, text="To Station:",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),100,350)
            lbl27=bkrgframe.add(tk.Label(deletewindow, text="Via:",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),100,400)
            lbl28=bkrgframe.add(tk.Label(deletewindow, text="Total Seats:",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),100,450)

            txt23=bkrgframe.add(tk.Entry(deletewindow,width=15),250,200)
            txt23.insert(0,a)
            txt24=bkrgframe.add(tk.Entry(deletewindow,width=15),250,250)
            txt24.insert(0,b)
            txt25=bkrgframe.add(tk.Entry(deletewindow,width=15),250,300)
            txt25.insert(0,c)
            txt26=bkrgframe.add(tk.Entry(deletewindow,width=15),250,350)
            txt26.insert(0,d)
            txt27=bkrgframe.add(tk.Entry(deletewindow,width=15),250,400)
            txt27.insert(0,e)
            txt28=bkrgframe.add(tk.Entry(deletewindow,width=15),250,450)
            txt28.insert(0,f)

            btn1=bkrgframe.add(tk.Button(deletewindow, text="Delete",bg="dark slate gray", font=("cambria",12,'bold'),fg="white",command=delete_submit),150,500)
            btn2=bkrgframe.add(tk.Button(deletewindow, text="Clear",bg="dark slate gray", font=("cambria",12,'bold'),fg="white",command=delete_clear),250,500)
        except Error as E:
            messagebox.showinfo('Please Try Again !!!',E)   
  
def delete_window():
    '''To create delete window'''
    global txt22,bkrgframe,deletewindow
    admin=adminwindow
    admin.destroy()
    deletewindow=Tk()
    Image_Path = 'Train 3.gif'
    Width,Height=700,600  
    deletewindow.title("Delete Train Details")
    deletewindow.geometry('{}x{}'.format(Width,Height))
    bkrgframe = BkgrFrame(deletewindow,Image_Path,Width,Height)
    bkrgframe.pack()
    deletewindow.resizable(width=False,height=False)
    
    lbl22=bkrgframe.add(tk.Label(deletewindow, text="Enter Train No. of Train to be deleted:",font=("cambria",12,'bold'),bg="dark slate gray",fg="white"),50,100)
    txt22=bkrgframe.add(tk.Entry(deletewindow,width=15),350,100)
    btn1=bkrgframe.add(tk.Button(deletewindow, text="Show Train Details",bg="dark slate gray", font=("cambria",12,'bold'),fg="white",command=delete_update),170,150)
    btn2=bkrgframe.add(tk.Button(deletewindow, text="Home",bg="dark slate gray", font=("cambria",12,'bold'),fg="white",command=delete_home),600,50)
    deletewindow.mainloop()

def admin_window():
    '''To create admin window'''
    global adminwindow,value,wind
    adminwindow = Tk()
    wind=1
    Image_Path = 'Train 5.gif'
    Width,Height=700,600

    adminwindow.title("Admin Window")
    adminwindow.geometry('{}x{}'.format(Width,Height))
    bkrgframe = BkgrFrame(adminwindow,Image_Path,Width,Height)
    bkrgframe.pack()

    btn1=bkrgframe.add(tk.Button(adminwindow,text="Add Train Details",bg="dark slate gray",font=("Arial Narrow",12,'bold'),fg="white",command=add_window),10,170)
    btn2=bkrgframe.add(tk.Button(adminwindow,text="Update Train Details",bg="dark slate gray",font=("Arial Narrow",12,'bold'),fg="white",command=update_window),150,170)
    btn3=bkrgframe.add(tk.Button(adminwindow,text="Delete Train Details",bg="dark slate gray",font=("Arial Narrow",12,'bold'),fg="white",command=delete_window),300,170)
    lgot=bkrgframe.add(tk.Button(adminwindow,text="Log Out",bg="dark slate gray",font=("Arial Narrow",12,'bold'),fg="white",command=logout),600,50)
    adminwindow.resizable(width=False,height=False)

def login2():
    '''To check whether username and password matches with ech other'''
    global value,result,x,txt1,txt2
    try:
        connection=sql.connect(host="localhost",user="root",passwd="root",database="WONDERAIL")
        cursor=connection.cursor()
        uname=txt1.get()
        passwd=txt2.get()
        if value==1:
            query="SELECT PASSWORD FROM ADMIN WHERE USERNAME='{}';".format(uname)
            cursor.execute(query)
            data=cursor.fetchall()
            for x in data:
                pword1=str(x)
                pword2=str((passwd,))
                if pword2==pword1:
                    messagebox.showinfo('LOGIN SUCCESS','You have been Logged in Successfully')
                    window.destroy()
                    admin_window()
                else:
                    messagebox.showinfo('LOGIN FAIL','Please check whether you have entered the correct Username & Password')
        elif value==2:
            query="SELECT PASSWORD FROM USER WHERE USERNAME='{}';".format(uname)
            cursor.execute(query)
            data=cursor.fetchall()
            for x in data:
                pword1=str(x)
                pword2=str((passwd,))
                if pword2==pword1:
                    messagebox.showinfo('LOGIN SUCCESS','You have been Logged in Successfully')
                    window.destroy()
                    user_window()
                else:
                    messagebox.showinfo('LOGIN FAIL','Please check whether you have entered the correct Username & Password')
        connection.close()
    except Error as E:
        messagebox.showinfo('Please Try Again !!!',E) 
        
def login1():
    '''To check whether username exit or not'''
    global value,result,x,txt1,txt2,uname
    try:
        connection=sql.connect(host="localhost",user="root",passwd="root",database="WONDERAIL")
        cursor=connection.cursor()
        uname=txt1.get()
        passwd=txt2.get()
        if value==1:
            query="SELECT USERNAME FROM ADMIN;"
            cursor.execute(query)
            data=cursor.fetchall()
            for x in data:
                uname1=str(x)
                uname2=str((uname,))
                if uname2==uname1:
                    abcd=1
                    break
                else:
                    abcd=0
            if abcd==1:
                login2()
            else:
                messagebox.showinfo('Login Fail','Please check whether you have entered the correct Username & Password')
        elif value==2:
            query="SELECT USERNAME FROM USER;"
            cursor.execute(query)
            data=cursor.fetchall()
            for x in data:
                uname1=str(x)
                uname2=str((uname,))
                if uname2==uname1:
                    abcd=1
                    break
                else:
                    abcd=0
            if abcd==1:
                login2()
            else:
                messagebox.showinfo('Login Fail','Please check whether you have entered the correct Username & Password')
        connection.close()
    except Error as E:
        messagebox.showinfo('Please Try Again !!!',E) 

def signup():
    '''To ensure that all details are filled and to ad user detials to mysql table user on clicking the button signup'''
    global txt9,txt10,txt11,txt12,txt13,txt14,signupwindow
    def signup1():
        '''To insert new user details to MySQL table user on clicking signup button'''
        global txt9,txt10,txt11,txt12,txt13,txt14,signupwindow
        try:
            a,b,c,d,e,f=txt9.get(),txt10.get(),txt11.get(),txt12.get(),txt13.get(),txt14.get()
            connection=sql.connect(host="localhost",user="root",passwd="root",database="WONDERAIL")
            cursor=connection.cursor()
            query="INSERT INTO USER VALUES('{}',{},{},'{}','{}','{}');".format(a,b,c,d,e,f)
            cursor.execute(query)
            connection.commit()
            connection.close()
            messagebox.showinfo("Successful","User Account is Successfully Created")
            signupwindow.destroy()
            mainwindow()
        
        except Error as E:
            messagebox.showinfo('Please Try Again !!!',E) 
    if not txt9.get() or not txt10.get() or not txt11.get() or not txt12.get() or not txt13.get() or not txt14.get():
        messagebox.showinfo("Invalid Details","Please ensure that all details are filled")
    else:
        signup1()

def signup_window():
    '''To create signupp window'''
    global txt9,txt10,txt11,txt12,txt13,txt14,signupwindow,window,wind
    wind=3
    window.destroy()
    signupwindow= Tk()
    swindow=signupwindow
    Image_Path = 'Train 2.gif'
    Width,Height=700,600

    swindow.title("Sign Up Window")
    swindow.geometry('{}x{}'.format(Width,Height))
    bkrgframe = BkgrFrame(swindow,Image_Path,Width,Height)
    bkrgframe.pack()
  
    lbl9=bkrgframe.add(tk.Label(swindow, text="Name",font=("Bodoni MT",12,'bold'),width=10,bg="dark slate gray",fg='white'),100,100)
    lbl10=bkrgframe.add(tk.Label(swindow, text="Age",font=("Bodoni MT",12,'bold'),width=10,bg='dark slate gray',fg='white'),100,150)
    lbl11=bkrgframe.add(tk.Label(swindow, text="Phone Number",font=("Bodoni MT",12,'bold'),width=10,bg='dark slate gray',fg='white'),100,200)
    lbl12=bkrgframe.add(tk.Label(swindow, text="Email Id",font=("Bodoni MT",12,'bold'),width=10,bg='dark slate gray',fg='white'),100,250)
    lbl13=bkrgframe.add(tk.Label(swindow, text="Username",font=("Bodoni MT",12,'bold'),width=10,bg='dark slate gray',fg='white'),100,300)
    lbl14=bkrgframe.add(tk.Label(swindow, text="Password",font=("Bodoni MT",12,'bold'),width=10,bg='dark slate gray',fg='white'),100,350)
    
    txt9=bkrgframe.add(tk.Entry(swindow,width=30),250,100)
    txt10=bkrgframe.add(tk.Entry(swindow,width=30),250,150)
    txt11=bkrgframe.add(tk.Entry(swindow,width=30),250,200)
    txt12=bkrgframe.add(tk.Entry(swindow,width=30),250,250)
    txt13=bkrgframe.add(tk.Entry(swindow,width=30),250,300)
    txt14=bkrgframe.add(tk.Entry(swindow,width=30,show='*'),250,350)

    btn1=bkrgframe.add(tk.Button(swindow, text="Sign Up",bg="dark slate gray", font=("cambria",12,'bold'),fg="white",command=signup),200,400)
    home=bkrgframe.add(tk.Button(swindow,text="Home",bg="dark slate gray",font=("Arial Narrow",12,'bold'),fg="white",command=logout),600,50)
    swindow.resizable(width=False,height=False)    

def userclick():
    '''Function to decide what to do on clicking User button'''
    global value
    value=2
    btn=bkrgframe.add(tk.Button(window, text="SIGN UP",bg="dark slate gray", width=10,font=("Arial Narrow",12,'bold'),fg="white",state='normal' ,command=signup_window),350,250)

def adminclick():
    '''Function to decide what to do on clicking Admin button'''
    global value
    value=1
    btn=bkrgframe.add(tk.Button(window, text="SIGN UP",bg="dark slate gray", width=10,font=("Arial Narrow",12,'bold'),fg="white",state='disabled' ,command=signup_window),350,250)


#MAIN PROGRAM STARTS HERE
def mainwindow():
      '''To create Main Window'''
      global bkrgframe,window,txt1,txt2,v
      Image_Path = 'Train 1.gif'
      Width,Height =500,600
      window=Tk()
      v=tk.IntVar()
      window.title("Wonderail")
      window.geometry('{}x{}'.format(Width,Height))
      bkrgframe=BkgrFrame(window,Image_Path,Width,Height)
      bkrgframe.pack()

      #Radio Button
      rad1=bkrgframe.add(tk.Radiobutton(window,text='Admin',bg="navajo white", padx=20,width=5,font=("Monotype Corsiva",12,'bold'),fg="red",value=1,variable=v,command=adminclick),220,100)
      rad2=bkrgframe.add(tk.Radiobutton(window,text='User',bg="navajo white",padx=20, width=5,font=("Monotype Corsiva",12,'bold'),fg="red",value=2,variable=v,command=userclick),330,100)
      rad2.select()
      userclick()
      
      lbl1=bkrgframe.add(tk.Label(window, text="USERNAME",font=("Bodoni MT",12,'bold'),width=10,bg="dark slate gray",fg='white'),220,150)
      lbl2=bkrgframe.add(tk.Label(window, text="PASSWORD",font=("Bodoni MT",12,'bold'),width=10,bg='dark slate gray',fg='white'),220,200)

      txt1=bkrgframe.add(tk.Entry(window,width=15),350,150)
      txt2=bkrgframe.add(tk.Entry(window,width=15,show='*'),350,200)


      btn1=bkrgframe.add(tk.Button(window, text="LOGIN",bg="dark slate gray", width=10,font=("Arial Narrow",12,'bold'),fg="white",command=login1),220,250)


      window.configure(background="dark slate gray")
      window.resizable(width=False,height=False)
      window.mainloop()
mainwindow()





 

