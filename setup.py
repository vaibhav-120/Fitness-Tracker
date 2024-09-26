from tkinter import *
from PIL import Image,ImageTk
import database,login

class Setup():
    def __init__(self) -> None:
        self.root = Tk()
        self.root.state("zoomed")
        self.root.title("Fitness Tracker-Setup")

        self.mainframe = Frame(self.root,width=1366,height=697,bg="black")
        self.mainframe.place(x=0,y=0)

        self.frame1 = Frame(self.mainframe,width=550, height=657,bg="#3e436c")
        self.frame1.place(x=20,y=20)

        self.frame2 = Frame(self.mainframe,width=776, height=657,bg="white")
        self.frame2.place(x=570,y=20)

        self.setlbl = Label(self.frame1,text="SETUP",bg="#3e436c",fg="white",font="Arial 32 bold")
        self.setlbl.place(x=50,y=40)
        self.sublbl = Label(self.frame1,text="Set your dream weight you want to achieve. Also enter the timeperiod under which you want to achieve your goal",bg="#3e436c",fg="white",font="Arial 17 bold",wraplength=400,justify="left")
        self.sublbl.place(x=50,y=120)

        self.fitimg = Image.open("images/fitness.png").resize((390,260))
        self.fitimgtk = ImageTk.PhotoImage(self.fitimg)
        self.fitimglbl = Label(self.frame1,image=self.fitimgtk,bg="#3e436c")
        self.fitimglbl.place(x=80,y=300)


        self.weight = 10
        self.time = 3
        self.weightgoallbl = Label(self.frame2,text="Weight You Want To Achieve",fg="#3e436c",font="Arial 25 bold",bg="white")
        self.weightgoallbl.place(x=50,y=50)
        self.weightlbl = Label(self.frame2,text="10",font="Arial 25 bold",bg="white")
        self.weightlbl.place(x=290,y=160)
        self.timelbl2 = Label(self.frame2,text="KG",font="Arial 25 bold",bg="white")
        self.timelbl2.place(x=330,y=160)
        self.weightentry = Scale(self.frame2,from_=10,to=99,orient=HORIZONTAL,length=500,bg="#3e436c",activebackground="#3e436c",bd=0,showvalue=0,command=self.weightval)
        self.weightentry.place(x=100,y=130)

        self.timegoallbl = Label(self.frame2,text="Time Period To Achieve Goal",fg="#3e436c",font="Arial 25 bold",bg="white")
        self.timegoallbl.place(x=50,y=300)
        self.timelbl = Label(self.frame2,text="3",font="Arial 25 bold",bg="white")
        self.timelbl.place(x=290,y=410)
        self.timelbl2 = Label(self.frame2,text="months",font="Arial 25 bold",bg="white")
        self.timelbl2.place(x=330,y=410)
        self.timeentry = Scale(self.frame2,from_=3,to=24,orient=HORIZONTAL,length=500,bg="#3e436c",activebackground="#3e436c",bd=0,showvalue=0,command=self.timeval)
        self.timeentry.place(x=100,y=380)


        self.setbtn = Button(self.frame2,text="Set",bg="#3e436c",fg="white",width=10,font="Arial 11 bold",command=self.savelog)
        self.setbtn.place(x=300,y=530)


        self.root.mainloop()

    def weightval(self,var):
        self.weight = var
        try:
            self.weightlbl.destroy()
        except:
            pass
        self.weightlbl = Label(self.frame2,text=self.weight,font="Arial 25 bold",bg="white")
        self.weightlbl.place(x=290,y=160)
    
    def timeval(self,var):
        self.time = var
        try:
            self.timelbl.destroy()
        except:
            pass
        self.timelbl = Label(self.frame2,text=self.time,font="Arial 25 bold",bg="white")
        self.timelbl.place(x=290,y=410)

    def savelog(self):
        # per day calories calculation
        content = database.fetchlastdetails()
        age = content[4]
        height = content[5]
        heightcm = (100 * height) 
        weight = content[6]
        gender = content[7]
        activity = content[8]
        goaltime = int(self.time)
        goalweight = int(self.weight)
        if gender == 'Male':
            BMR = (10 * weight) + (6.25 * heightcm) - (5* age) + 5
        else:
            BMR = (10 * weight) + (6.25 * heightcm) - (5* age) - 161

        if activity == 'Very Little':
            const = 1.2
        elif activity == 'Little':
            const = 1.375
        elif activity == 'Moderate':
            const = 1.55
        elif activity == 'Heavy':
            const = 1.725
        else:
            const = 1.9
        
        AMR = BMR * const

        weight_increase = goalweight - weight
        weeks = round(goaltime*4.34524)
        perweekweight = weight_increase/weeks

        perkg = 1000
        perdaycalorie = (perkg * perweekweight) + AMR

        perdayfat = (perdaycalorie * 0.3)/9
        perdayprotein = (perdaycalorie * 0.2)/4
        perdaycarbs = (perdaycalorie * 0.5)/4

        database.updateval((self.weight,self.time,perdaycalorie,perdayfat,perdaycarbs,perdayprotein),weight)
        self.root.destroy()
        login.Signin()


if __name__ == "__main__":
    Setup()