from tkinter import *
from PIL import Image, ImageTk
import weight_tracker,meal_track,workout_track,meal_generator


class FrontDetails():
    def __init__(self, frame,res) -> None:
        self.res = res
        self.content_panel = frame

        # content1
        self.waternecessary = 7
        self.watercount = 0
        # frame1        
        self.img1 = Image.open("images/content_bg.png").resize((1200,600))
        self.img1tk = ImageTk.PhotoImage(self.img1)
        self.lbl = Label(self.content_panel,image=self.img1tk,bd=0)
        self.lbl.place(x=0,y=40)

        self.glassimg = Image.open("images/glass_water.png").resize((60,80))
        self.glassimgtk = ImageTk.PhotoImage(self.glassimg)
        self.glassimglbl = Label(self.content_panel,image=self.glassimgtk,bg="#EBEBEB",bd=0)
        self.glassimglbl.place(x=180,y=185)

        self.addimg = Image.open("images/add.png").resize((50,50))
        self.addimgtk = ImageTk.PhotoImage(self.addimg)
        self.addbtn = Button(self.content_panel,image=self.addimgtk,bg="#cbc8c8",bd=0,command=self.wateradd)
        self.addbtn.place(x=340,y=145)

        self.subimg = Image.open("images/sub.png").resize((50,50))
        self.subimgtk = ImageTk.PhotoImage(self.subimg)
        self.subbtn = Button(self.content_panel,image=self.subimgtk,bg="#cbc8c8",bd=0,command=self.watersub)
        self.subbtn.place(x=30,y=145)
        

        self.waterlbl3 = Label(self.content_panel,text="Drink",bg="#cbc8c8",font="Arial 20 bold")
        self.waterlbl3.place(x=150,y=85)
        self.waterlbl2 = Label(self.content_panel,text="glass(s) of water",bg="#cbc8c8",font="Arial 17 bold")
        self.waterlbl2.place(x=120,y=135)
        self.waterlbl1 = Label(self.content_panel,text="7",bg="#cbc8c8",font="Arial 30 bold")
        self.waterlbl1.place(x=230,y=75)



        # content2
        self.weighttrackimg = Image.open("images/weight_logo.png").resize((70,70))
        self.weighttrackimgtk = ImageTk.PhotoImage(self.weighttrackimg)
        
        self.weighttrackbtn = Button(self.content_panel,text="Weight Tracker",font="Arial 24 bold",fg="#8b29a3",image=self.weighttrackimgtk,bg="#cbc8c8",bd=0,height=100,compound=LEFT,command=self.weighttrackgraph)
        self.weighttrackbtn.place(x=608,y=80)



        # content3
        self.mealtrackimg = Image.open("images/meal_logo.png").resize((70,70))
        self.mealtrackimgtk = ImageTk.PhotoImage(self.mealtrackimg)

        self.mealtrackbtn = Button(self.content_panel,text="Calorie Tracker",font="Arial 24 bold",fg="#ff4d00",image=self.mealtrackimgtk,height=100,bg="#cbc8c8",bd=0,compound=LEFT,command=self.calorietrackfn)
        self.mealtrackbtn.place(x=608,y=255)


        # content4
        self.workouttrackimg = Image.open("images/workout_logo.png").resize((70,70))
        self.workouttrackimgtk = ImageTk.PhotoImage(self.workouttrackimg)

        self.workouttrackbtn = Button(self.content_panel,text="Workout Tracker",font="Arial 24 bold",fg="green",image=self.workouttrackimgtk,height=100,bg="#cbc8c8",bd=0,compound=LEFT,command=self.workouttrackfn)
        self.workouttrackbtn.place(x=600,y=430)


        # content5
        self.mealgenerateimg = Image.open("images/diet_logo.png").resize((100,100))
        self.mealgenerateimgtk = ImageTk.PhotoImage(self.mealgenerateimg)

        self.mealgeneratebtn = Button(self.content_panel,text="Meal Generator",font="Arial 26 bold",fg="red",image=self.mealgenerateimgtk,height=200,bg="#cbc8c8",bd=0,compound=BOTTOM,command=self.mealgeneratefn)
        self.mealgeneratebtn.place(x=82,y=350)



    def wateradd(self):
        try:
            self.waterlbl1.destroy()
            self.waterlbl2.destroy()
            self.waterlbl3.destroy()
        except:
            pass
        
        self.watercount = self.watercount + 1
        if self.watercount == 7:
            self.waterlbl1 = Label(self.content_panel,text="Today's Goal Completed",bg="#cbc8c8",font="Arial 20 bold")
            self.waterlbl1.place(x=50,y=95)
        else:
            self.waterlbl1 = Label(self.content_panel,text=self.watercount,bg="#cbc8c8",font="Arial 25 bold")
            self.waterlbl1.place(x=147,y=85)
            self.waterlbl2 = Label(self.content_panel,text=" of 7",bg="#cbc8c8",font="Arial 25 bold")
            self.waterlbl2.place(x=185,y=85)
            self.waterlbl3 = Label(self.content_panel,text="glasses",bg="#cbc8c8",font="Arial 20 bold")
            self.waterlbl3.place(x=155,y=135)

    def watersub(self):
        if not(self.watercount < 8):
            try:
                self.waterlbl1.destroy()
            except:
                pass

        if self.watercount > 0:
            self.watercount = self.watercount - 1
            self.waterlbl1 = Label(self.content_panel,text=self.watercount,bg="#cbc8c8",font="Arial 25 bold")
            self.waterlbl1.place(x=147,y=85)
        else:
            pass

    def weighttrackgraph(self):
        weight_tracker.WeightTracker(self.content_panel,self.res)

    def calorietrackfn(self):
        meal_track.MealTracker(self.content_panel,self.res)

    def workouttrackfn(self):
        workout_track.WorkoutTracker(self.content_panel,self.res)

    def mealgeneratefn(self):
        meal_generator.meal_generator(self.content_panel,self.res)