from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from datetime import date
import database,dashboard,BMICalculator

class Signin():
    def __init__(self, *data):
        self.data = data
        self.root = Tk()
        self.root.state("zoomed")
        self.root.title("Fitness Tracker - Login")
        self.root.resizable(False,False)

        self.mainframe = Frame(self.root,width=1366,height=697,bg="black")
        self.mainframe.place(x=0,y=0)

        self.frame = Frame(self.mainframe, width=663, height=657, bg="white")
        self.frame.place(x=20,y=20)

        self.wlcmlbl = Label(self.frame,text="WELCOME",font="Arial 35 bold",bg="white")
        self.wlcmlbl.place(x=150,y=80)

        self.img1 = Image.open("Logo.png")
        self.imgtk1 = ImageTk.PhotoImage(self.img1)
        self.imglbl = Label(self.frame,image=self.imgtk1,bg="white")
        self.imglbl.place(x=150,y=150)
        self.lbl1 = Label(self.frame,text="Fitness Tracker",font="Arial 30 bold",bg="white")
        self.lbl1.place(x=135,y=400)
        self.lbl2 = Label(self.frame,text="Track your Food & Workout",font="Arial 15",bg="white")
        self.lbl2.place(x=150,y=450)

        self.frame2 = Frame(self.mainframe,width=663, height=657, bg="white")
        self.frame2.place(x=683,y=20)

        self.signin_label = Label(self.frame2,text="Sign in", bg="white", fg="#5d64a2", font="Arial 30 bold")
        self.signin_label.place(x=120,y=100)

        # For username
        self.userlbl = Label(self.frame2,text="Username", bg="white", font="Arial 17 bold")
        self.userlbl.place(x=0,y=190)
        self.user_entry = Entry(self.frame2, width=30, font="Arial 12", border=0)
        self.user_entry.place(x=180,y=196)
        self.underline1 = Frame(self.frame2,width=270, height=2, bg="black")
        self.underline1.place(x=180,y=216)

        # For password
        self.passlbl = Label(self.frame2,text="Password", bg="white", font="Arial 17 bold")
        self.passlbl.place(x=0,y=280)
        self.pass_entry = Entry(self.frame2, width=30, font="Arial 12", border=0,show="*")
        self.pass_entry.place(x=180,y=286)
        self.underline2 = Frame(self.frame2,width=270, height=2, bg="black")
        self.underline2.place(x=180,y=306)

        # For button
        self.loginbtn = Button(self.frame2,text="Sign in",bg="#5d64a2",width=40,border=0,height=2,fg="white",cursor="hand2",font="Arial 10 bold",command=self.enter)
        self.loginbtn.place(x=60,y=390)

        # For New user
        self.signup_lbl = Label(self.frame2,text="Don't have an account?",bg="white",font="Arial 13")
        self.signup_lbl.place(x=80,y=440)
        self.signup_btn = Button(self.frame2,text="Sign up",border=0, fg="#5d64a2", cursor="hand2",bg="white",font="Arial 13",command=self.signup)
        self.signup_btn.place(x=260,y=438)

        self.root.mainloop()

    def signup(self):
        self.root.destroy()
        BMICalculator.BMI()

    def enter(self):
        if not(self.user_entry.get()) and not(self.pass_entry.get()):
            messagebox.showwarning("Warning","Enter Username and Password")
        elif not(self.user_entry.get()):
            messagebox.showwarning("Warning","Username is required")
        elif not(self.pass_entry.get()):
            messagebox.showwarning("Warning","Password is required")
        else:
            res = database.loginUser((self.user_entry.get(),self.pass_entry.get()))
            if res:
                self.root.destroy()
                today = date.today()
                # print(database.checkdate(today))
                dashboard.Dashboard(res)
            else:
                messagebox.showinfo("Warning","Wrong Username or Password")

if __name__ == "__main__":
    Signin()