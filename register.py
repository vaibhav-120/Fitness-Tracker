from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import login,re,setup,database

class Register():
    def __init__(self,data):
        self.age_weight_height = data
        self.root = Tk()
        self.root.state("zoomed")
        self.root.title("Fitness Tracker - Register")
        self.root.resizable(False,False)

        self.mainframe = Frame(self.root,width=1366,height=697,bg="black")
        self.mainframe.place(x=0,y=0)

        self.frame = Frame(self.mainframe, width=663, height=657, bg="white")
        self.frame.place(x=20,y=20)

        self.wlcmlbl = Label(self.frame,text="WELCOME",font="Arial 35 bold",bg="white")
        self.wlcmlbl.place(x=150,y=80)

        self.img1 = Image.open("images/Loginimg.png").resize((250,250))
        self.imgtk1 = ImageTk.PhotoImage(self.img1)
        self.imglbl = Label(self.frame,image=self.imgtk1,bg="white")
        self.imglbl.place(x=150,y=150)
        self.lbl1 = Label(self.frame,text="Fitness Tracker",font="Arial 30 bold",bg="white")
        self.lbl1.place(x=135,y=400)
        self.lbl2 = Label(self.frame,text="Track your Food & Workout",font="Arial 15",bg="white")
        self.lbl2.place(x=150,y=450)

        self.frame2 = Frame(self.mainframe,width=663, height=657, bg="white")
        self.frame2.place(x=683,y=20)

        self.signin_label = Label(self.frame2,text="Register", bg="white", fg="#5d64a2", font="Arial 30 bold")
        self.signin_label.place(x=120,y=100)

        # For E-mail
        self.maillbl = Label(self.frame2,text="E-mail", bg="white", font="Arial 17 bold")
        self.maillbl.place(x=0,y=190)
        self.mail_entry = Entry(self.frame2, width=30, font="Arial 12", border=0)
        self.mail_entry.place(x=180,y=196)
        self.underline = Frame(self.frame2,width=270, height=2, bg="black")
        self.underline.place(x=180,y=216)

        # For username
        self.userlbl = Label(self.frame2,text="Username", bg="white", font="Arial 17 bold")
        self.userlbl.place(x=0,y=280)
        self.user_entry = Entry(self.frame2, width=30, font="Arial 12", border=0)
        self.user_entry.place(x=180,y=286)
        self.underline1 = Frame(self.frame2,width=270, height=2, bg="black")
        self.underline1.place(x=180,y=306)

        # For password
        self.passlbl = Label(self.frame2,text="Password", bg="white", font="Arial 17 bold")
        self.passlbl.place(x=0,y=370)
        self.pass_entry = Entry(self.frame2, width=30, font="Arial 12", border=0,show="*")
        self.pass_entry.place(x=180,y=376)
        self.underline2 = Frame(self.frame2,width=270, height=2, bg="black")
        self.underline2.place(x=180,y=396)

        # For button
        self.loginbtn = Button(self.frame2,text="Sign up",bg="#5d64a2",width=40,border=0,height=2,fg="white",cursor="hand2",font="Arial 10 bold",command=self.creation)
        self.loginbtn.place(x=60,y=450)

        # For Existing user
        self.signup_lbl = Label(self.frame2,text="Already have an account?",bg="white",font="Arial 13")
        self.signup_lbl.place(x=80,y=500)
        self.signup_btn = Button(self.frame2,text="Sign in",border=0, fg="#5d64a2", cursor="hand2",bg="white",font="Arial 13", command=self.signin )
        self.signup_btn.place(x=260,y=498)

        self.root.mainloop()

    def signin(self):
        self.root.destroy()
        login.Signin()
    def creation(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if not(self.mail_entry.get()) or not(self.user_entry.get()) or not(self.pass_entry.get()):
            messagebox.showwarning("Warning","Please enter all the fields")
        elif not(re.fullmatch(regex, self.mail_entry.get())):
            messagebox.showwarning("Warning","Invalid Mail ID!")
        elif not(self.user_entry.get().strip()):
            messagebox.showinfo("Username","Invalid Username!")
        elif (len(self.pass_entry.get()) < 7):
            messagebox.showinfo("Password","Password length should be at least 8 character long")
        else:
            details = (self.mail_entry.get(),self.user_entry.get(),self.pass_entry.get(),self.age_weight_height[0],self.age_weight_height[1],self.age_weight_height[2],self.age_weight_height[3],self.age_weight_height[4])
            res = database.registerUser(details)
            if res[0]:
                messagebox.showinfo("Registration","Account created successfully")
                self.root.destroy()
                setup.Setup()
            else:
                # error for already existed email or username
                if 'username' in res[1]:
                    messagebox.showerror('Alert', 'Username already taken.')
                if 'email' in res[1]:
                    messagebox.showerror('Alert', 'Email is already registered.')


if __name__ == "__main__":
    Register(5)