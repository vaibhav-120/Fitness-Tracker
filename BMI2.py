from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import register,login,dashboard

class BMI():
    def __init__(self,res):
        self.res = res
        self.root = Tk()
        self.root.state("zoomed")
        self.root.title("BMI Calculator")
        
        self.bg = Frame(self.root,width=1366,height=697,bg="black")
        self.bg.place(x=0,y=0)

        self.mainframe = Frame(self.bg,width=1326,height=657,bg="#cbc8c8")
        self.mainframe.place(x=20,y=20)

        self.left_panel = Frame(self.mainframe,width=500,height=617,bg="white")
        self.left_panel.place(x=20,y=20)

        # heading
        self.headlbl = Label(self.left_panel,text="BMI Calculator",font="Arial 25 bold",bg="white")
        self.headlbl.place(x=20,y=20)
        self.head2lbl = Label(self.left_panel,text="Please fill the details below",font="Arial 10 bold",bg="white")
        self.head2lbl.place(x=25,y=70)

        # age input
        self.agelbl = Label(self.left_panel,text="Age",font="Arial 15 bold",bg="white")
        self.agelbl.place(x=25,y=115)
        self.ageinp = Entry(self.left_panel,width=8,font="Arial 10 bold",bd=3)
        self.ageinp.place(x=150,y=120)

        # height input
        self.heightlbl = Label(self.left_panel,text="Height",font="Arial 15 bold",bg="white")
        self.heightlbl.place(x=25,y=175)
        self.heightinp = Entry(self.left_panel,width=8,font="Arial 10 bold",bd=3)
        self.heightinp.place(x=150,y=180)
        self.click = StringVar()
        self.click.set("Units")
        self.heightunit = False
        self.heightunits = OptionMenu(self.left_panel,self.click,"inch","cm","yards",command=self.user_height_unit)
        self.heightunits.place(x=250,y=175)

        # weight input
        self.weightlbl = Label(self.left_panel,text="Weight",font="Arial 15 bold",bg="white")
        self.weightlbl.place(x=25,y=235)
        self.weightinp = Entry(self.left_panel,width=8,font="Arial 10 bold",bd=3)
        self.weightinp.place(x=150,y=240)
        self.click2 = StringVar()
        self.click2.set("Units")
        self.weightunit = False
        self.weightunits = OptionMenu(self.left_panel,self.click2,"KG","lbs",command=self.user_weight_unit)
        self.weightunits.place(x=250,y=235)

        # gender input
        self.genderlbl = Label(self.left_panel,text="Gender",font="Arial 15 bold",bg="white")
        self.genderlbl.place(x=25,y=295)
        self.gender = StringVar()
        self.gender.set("Select Gender")
        self.genderval = False
        self.genderdd = OptionMenu(self.left_panel,self.gender,"Male","Female",command=self.usergender)
        self.genderdd.place(x=150,y=300)

        self.activitylbl = Label(self.left_panel,text="Activity",font="Arial 15 bold",bg="white")
        self.activitylbl.place(x=25,y=355)
        self.activity = StringVar()
        self.activity.set("Select Activity Level")
        self.activityval = False
        self.activitydd = OptionMenu(self.left_panel,self.activity,"Very Little","Little","Moderate","Heavy","Intense",command=self.activityfn)
        self.activitydd.place(x=150,y=360)

        # Calculate button
        self.calbtn = Button(self.left_panel,text="Calculate",width=20,height=1,bg="#2d2e3d",fg="white",font="Arial 15 bold",command=self.calculate)
        self.calbtn.place(x=70,y=460)

        # right content
        self.right_top_panel = Frame(self.mainframe,width=750,height=635,bg="white")
        self.right_top_panel.place(x=550,y=20)

        self.reglbl = Label(self.right_top_panel,text="Start your Fitness Journey with us",font="Arial 20 bold",bg="white")
        self.reglbl.place(x=30,y=70)
        self.reglbl2 = Label(self.right_top_panel,text="BMI is a measurement of a person's leanness or corpulence based on their height and weight, and is intended to quantify tissue mass.",font="Arial 10 bold",wraplength=600,justify="left",bg="white")
        self.reglbl2.place(x=30,y=110)

        self.img2 = Image.open("images/BMI_demo.png").resize((210,210))
        self.img2tk = ImageTk.PhotoImage(self.img2)
        self.img2lbl = Label(self.right_top_panel,image=self.img2tk,bg="white")
        self.img2lbl.place(x=50,y=180)

        self.info1lbl = Label(self.right_top_panel,text="Underweight",font="Arial 10 bold",bg="white")
        self.info1lbl.place(x=300,y=180)
        self.infofrm = Frame(self.right_top_panel,bg="#3487FF",width=20,height=20)
        self.infofrm.place(x=400,y=180)
        
        self.info2lbl = Label(self.right_top_panel,text="Normal",font="Arial 10 bold",bg="white")
        self.info2lbl.place(x=300,y=220)
        self.info2frm = Frame(self.right_top_panel,bg="#4FA84F",width=20,height=20)
        self.info2frm.place(x=400,y=220)
        
        self.info3lbl = Label(self.right_top_panel,text="Overweight",font="Arial 10 bold",bg="white")
        self.info3lbl.place(x=300,y=260)
        self.info3frm = Frame(self.right_top_panel,bg="#F33B3B",width=20,height=20)
        self.info3frm.place(x=400,y=260)

        self.logbtn = Button(self.right_top_panel,text="Go Back",width=10,bg="#2d2e3d",fg="white",font="Arial 12 bold",command=self.gobackfn)
        self.logbtn.place(x=600,y=20)


        self.root.mainloop()

    def usergender(self,val):
        self.genderval = val
    def activityfn(self,val):
        self.activityval = val
    def user_height_unit(self,val):
        self.heightunit = val
    def user_weight_unit(self,val):
        self.weightunit = val
    def gobackfn(self):
        self.root.destroy()
        dashboard.Dashboard(self.res)
    def logfnc(self):
        data = (int(self.ageinp.get()),self.heightval,self.weightval,self.genderval,self.activityval)
        self.root.destroy()
        register.Register(data)
    def loginfn(self):
        self.root.destroy()
        login.Signin()

    def calculate(self):
        try:
            self.condition1lbl.destroy()
            self.condition2lbl.destroy()
        except:
            pass
        age = self.ageinp.get()
        height = self.heightinp.get()
        weight = self.weightinp.get()
        gender = self.genderval
        wunit = self.weightunit
        hunit = self.heightunit
        activity = self.activityval
        if not(age) or not(height) or not(weight):
            messagebox.showwarning("Warning","Fill all fields")
        elif not(hunit):
            messagebox.showwarning("Warning","Select units for Height")
        elif not(wunit):
            messagebox.showwarning("Warning","Select units for Weight")
        elif not(gender):
            messagebox.showwarning("Warning","Select your Gender")
        elif not(activity):
            messagebox.showwarning("Warning","Select your Activity Level")
        else:
            try:
                age = int(age)
                height = int(height)
                weight = int(weight)
            except:
                messagebox.showwarning("Warning","Enter numeric values only")
        if type(age) == int and type(height) == int and type(weight) == int:
            if wunit == "lbs":
                weight = 0.45359237 * weight
                wunit = "KG"
            if hunit == "cm":
                height = height/100
                hunit = "m"
            elif hunit == "yards":
                height = 0.9144 * height
                hunit = "m"
            elif hunit == "inch":
                height = height/39.37
                hunit = "m"
            self.weightval = weight
            self.heightval = height
            self.bmi = round((weight/(height*height)),2)

            if age >= 20:
                if self.bmi < 16:
                    health = "Severe Thinness"
                elif self.bmi <= 17:
                    health = "Moderate Thinness"
                elif self.bmi <= 18.5:
                    health = "Mild Thinness"
                elif self.bmi <= 25:
                    health = "Normal"
                elif self.bmi <= 30:
                    health = "Overweight"
                else:
                    health = "Obese"
            else:
                if self.bmi < 16:
                    health = "Severe Thinness"
                elif self.bmi <= 17:
                    health = "Moderate Thinness"
                elif self.bmi <= 18.5:
                    health = "Mild Thinness"
                elif self.bmi <= 25:
                    health = "Normal"
                elif self.bmi <= 30:
                    health = "Overweight"
                else:
                    health = "Obese"
            
            if health == "Severe Thinness" or health == "Moderate Thinness" or health == "Mild Thinness":
                self.imginfo1 = Image.open("images/BMI_underweight.png").resize((210,210))
                self.imginfo1tk = ImageTk.PhotoImage(self.imginfo1)
                self.imginfo1lbl= Label(self.right_top_panel,image=self.imginfo1tk,bg="white")
                self.imginfo1lbl.place(x=50,y=180)
            elif health == "Normal":
                self.imginfo2 = Image.open("images/BMI_normal.png").resize((210,210))
                self.imginfo2tk = ImageTk.PhotoImage(self.imginfo2)
                self.imginfo2lbl= Label(self.right_top_panel,image=self.imginfo2tk,bg="white")
                self.imginfo2lbl.place(x=50,y=180)
            else:
                self.imginfo3 = Image.open("images/BMI_overweight.png").resize((210,210))
                self.imginfo3tk = ImageTk.PhotoImage(self.imginfo3)
                self.imginfo3lbl= Label(self.right_top_panel,image=self.imginfo3tk,bg="white")
                self.imginfo3lbl.place(x=50,y=180)
            

            self.desc_lbl = Label(self.right_top_panel,text="Result",font="Arial 25 bold",bg="white")
            self.desc_lbl.place(x=450,y=350)
            self.reslbl = Label(self.right_top_panel,text="Your BMI is :",bg="white",font="Arial 15 bold")
            self.reslbl.place(x=450,y=400)
            self.bmilbl = Label(self.right_top_panel,text=self.bmi,font="Arial 15 bold",bg="white")
            self.bmilbl.place(x=600,y=400)

            self.condition1lbl = Label(self.right_top_panel,text=health,bg="white",font="Arial 30 bold")
            self.condition1lbl.place(x=450,y=495)




if __name__ == "__main__":
    BMI()