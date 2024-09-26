from tkinter import *
from PIL import Image,ImageTk
import login,frontDetails,BMI2

class Dashboard():
    def __init__(self,res) -> None:
        self.res = res
        self.root = Tk()
        self.root.state("zoomed")
        self.root.resizable(False,False)
        self.root.title("Fitness Tracker")

        self.bgimg = Image.open("images/bg.png")
        self.bgimgtk = ImageTk.PhotoImage(self.bgimg)
        self.bglbl = Label(self.root,image=self.bgimgtk)
        self.bglbl.place(x=-2,y=0)

        self.side_panel = Frame(self.bglbl,bg="#2a184a",width=189,height=710)
        self.side_panel.place(x=0,y=34)

        self.top_panel = Frame(self.bglbl,bg="#473f77",width=860,height=117)
        self.top_panel.place(x=507,y=0)

        self.content_panel = Frame(self.bglbl,bg="white",width=1131,height=625)
        self.content_panel.place(x=240,y=118)

        self.headingframe = Frame(self.bglbl,bg="#2a184a",width=250,height=60)
        self.headingframe.place(x=220,y=50)
        self.headinglbl = Label(self.headingframe,text="Fitness Tracker",bg="#2a184a",fg="white",font="Arial 20 bold")
        self.headinglbl.place(x=25,y=10)

        self.userimg = Image.open("images/user_logo.png").resize((80,80))
        self.userimgtk = ImageTk.PhotoImage(self.userimg)
        self.userimglbl = Label(self.side_panel,image=self.userimgtk,bd=0)
        self.userimglbl.place(x=40,y=20)

        self.logoutlbl = Label(self.top_panel,text="Sign out",font="Arial 13 bold",bg="#473f77",fg="white")
        self.logoutlbl.place(x=720,y=42)


        # logout
        self.logoutimg = Image.open("images/logout.png").resize((45,45))
        self.logoutimgtk = ImageTk.PhotoImage(self.logoutimg)
        self.logout = Button(self.top_panel,image=self.logoutimgtk,bd=0,bg="#473f77",command=self.logoutfn)
        self.logout.place(x=800,y=30)


        # Dashboard
        self.dashboardbtn = Button(self.side_panel,text="Dashboard",bg="grey",fg="white",bd=0,font="Arial 15",width=17,command=self.dashboardfn)
        self.dashboardbtn.place(x=0,y=200)


        # BMI
        self.BMIbtn = Button(self.side_panel,text="BMI",bg="grey",fg="white",bd=0,font="Arial 15",width=17,command=self.bmifn)
        self.BMIbtn.place(x=0,y=250)









        frontDetails.FrontDetails(self.content_panel,self.res)
        self.root.mainloop()

    def logoutfn(self):
        self.root.destroy()
        login.Signin()

    def bmifn(self):
        self.root.destroy()
        BMI2.BMI(self.res)

    def dashboardfn(self):
        try:
            for widget in self.content_panel.winfo_children():
                widget.destroy()
        except:
            pass
        frontDetails.FrontDetails(self.content_panel,self.res)

if __name__ == "__main__":
    Dashboard()