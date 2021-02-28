import tkinter as tk
from tkinter import *
import bestdeveloper
top = tk.Tk()
# Functions and Logic
def newLabel(lname,text):
 (lname) = tk.Label(top, text = text)
 (lname).pack()
def newButton(bname,text,onclick):
 (bname) = tk.Button(top, text = text, command = onclick)
 (bname).pack()
def newLabelWithPlace(lname,text,x,y):
 (lname) = tk.Label(top, text = text).place(x=x,y=y)
def dashboard():
    print("xxx")
def signin():
    print("200")
    tk.destroy()
    dashboard()
def reset():
    for child in app.winfo_children():
        child.destroy()
newLabel("heading","Sign In to Dashboard - BestDeveloper")
newLabelWithPlace("email","Email: ",40,60)
newLabelWithPlace("pwd","Passsword: ",40,100)      
submit_button = Button(top,text = "Sign In", command=signin()).place(x = 40, y = 130)     
user_name_input_area = Entry(top, 
                             width = 30).place(x = 110, 
                                               y = 60)
user_password_entry_area = Entry(top, 
                                 width = 30,show = '*').place(x = 110, 
                                                   y = 100)   
top.mainloop()
