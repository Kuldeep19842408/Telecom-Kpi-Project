import tkinter as tk
import pandas as pd
win=tk.Tk()
win.geometry("400x400")
Name=tk.StringVar()
User=tk.StringVar()
Pass=tk.StringVar()
Confirmpassword=tk.StringVar()
Calender=tk.StringVar()

def checkNamefunction(X):
	for i in X:
		if ord(i)>=48 and ord(i)<=57:
			return False
	return True
label= tk.Label(win,text="")
def submit():
	label.configure(text="")
	Names=Name.get()
	if checkNamefunction(Names)==False:
		label.configure(text="Invalid Name")
		return
	Username=User.get()
	Password=Pass.get()
	Confirmpasswords=Confirmpassword.get()
	Name.set("")
	User.set("")
	Pass.set("")
	Confirmpassword.set("")

Name1=tk.Label(win,text="Name",fg="black")
Username1=tk.Label(win,text="Username",fg="black")
Password1=tk.Label(win,text="Password",fg="black")
Confirmpassword1=tk.Label(win,text="Confirmpassword",fg="black")

Nameentry=tk.Entry(win,textvariable=Name)
Userentry=tk.Entry(win,textvariable=User)
Passentry=tk.Entry(win,textvariable=Pass,show="*")
Confirmpassentry=tk.Entry(win,textvariable=Confirmpassword,show="*")
button=tk.Button(win,text="signup",command=submit)


Name1.grid(row=1,column=0)
Nameentry.grid(row=1,column=1)
Username1.grid(row=2,column=0)
Userentry.grid(row=2,column=1)
Password1.grid(row=3,column=0)
Passentry.grid(row=3,column=1)
Confirmpassword1.grid(row=4,column=0)
Confirmpassentry.grid(row=4,column=1)
button.grid(row=6,column=1)
label.grid(row=6,column=2)
win.mainloop()
