from tkinter import *
from tkinter import ttk
import database,workout_tracker_details
from tkinter import messagebox

class WorkoutTracker():
    def __init__(self,content,res):
        self.res = res
        self.content = content
        for widget in self.content.winfo_children():
            widget.destroy()
        
        self.headinglbl = Label(self.content,text="Workout Tracker",font=("Microsoft YaHei UI", 20, "bold"),bg="white")
        self.headinglbl.place(x=400,y=10)

        self.rightframe = Frame(self.content,width=250,height=200,bg="#505050")
        self.rightframe.place(x=880,y=50)

        self.dropdown = ttk.Combobox(self.rightframe, values=["back","cardio","chest","lower arms","lower legs","neck","shoulders","upper arms","upper legs","waist"])
        self.dropdown.place(x=20,y=50)
        self.dropdown.set("Select Muscle")
        self.dropdown.bind("<<ComboboxSelected>>")

        self.dropdown2 = ttk.Combobox(self.rightframe, values=['body weight', 'cable', 'leverage machine', 'assisted', 'medicine ball', 'stability ball', 'band', 'barbell', 'rope', 'dumbbell', 'ez barbell', 'sled machine', 'upper body ergometer', 'kettlebell', 'olympic barbell', 'weighted', 'bosu ball', 'resistance band', 'roller', 'skierg machine', 'hammer', 'smith machine', 'wheel roller', 'stationary bike', 'tire', 'trap bar', 'elliptical machine', 'stepmill machine'])
        self.dropdown2.place(x=20,y=100)
        self.dropdown2.set("Select Equipment")
        self.dropdown2.bind("<<ComboboxSelected>>")

        self.fetchbtn = Button(self.rightframe,text="Get Exercise",command=self.fetchfn)
        self.fetchbtn.place(x=50,y=150)
        
        
    def fetchfn(self):
        if self.dropdown.get() != "Select Muscle" and self.dropdown2.get() != "Select Equipment":
            self.muscle = self.dropdown.get()
            self.equipment = self.dropdown2.get()
            data = database.provide_exercise()
            exercise = []
            exercisegif = []
            for i in data:
                if i['bodyPart'] == self.muscle and i['equipment'] == self.equipment:
                    exercise.append(i['name'])
                    exercisegif.append(i['gifUrl'])
            workout_tracker_details.ExerciseDetails(self.content,self.res,exercise,exercisegif)
        else:
            messagebox.showwarning("Warning","Enter all fields")


if __name__ == "__main__":
    WorkoutTracker()