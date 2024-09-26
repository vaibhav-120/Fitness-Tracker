from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from datetime import date
import database

class meal_generator():
    def __init__(self,content,res):
        self.res = res
        self.content = content
        for widget in self.content.winfo_children():
            widget.destroy()
        # minCalories minProtein minCarbs minFat
        
        # heading
        self.heading = Label(self.content,text="Meal Generator",font="Arial 24 bold",bg="white")
        self.heading.place(x=25,y=25)

        # Cuisine
        self.cuisineinputlbl = Label(self.content,text="Enter your cuisine : ",bg="white")
        self.cuisineinputlbl.place(x=25,y=150)
        self.cuisine = StringVar()
        self.cuisine.set("Select Cuisine")
        self.cuisineval = False
        self.cuisinedd = OptionMenu(self.content,self.cuisine,"Indian","Italian",command=self.cuisinefn)
        self.cuisinedd.place(x=200,y=150)

        # diet type -veg or nonveg
        self.dietinputlbl = Label(self.content,text="Enter your cuisine : ",bg="white")
        self.dietinputlbl.place(x=25,y=220)
        self.diet = StringVar()
        self.diet.set("Select Cuisine")
        self.dietval = False
        self.dietdd = OptionMenu(self.content,self.diet,"vegetarian","nonvegetarian",command=self.dietfn)
        self.dietdd.place(x=200,y=220)
        #done button
        self.doneinputlbl = Label(self.content,text="Create Meal plan for : ",bg="white")
        self.doneinputlbl.place(x=25,y=290)
        self.done = StringVar()
        self.done.set("Select timezone")
        self.doneval = False
        self.donedd = OptionMenu(self.content,self.done,"Breakfast","Morning Snack","Lunch","Evening Snack","Dinner",command=self.donefn)
        self.donedd.place(x=200,y=290)

        self.donebutton = Button(self.content,text="Generate",font="Arial 10 bold",command=self.donebtnfn)
        self.donebutton.place(x=70,y=350)

    def cuisinefn(self,val):
        self.cuisineval = val

    def dietfn(self,val):
        self.dietval = val

    def donefn(self,val):
        self.doneval = val
        if self.doneval == "Morning Snack" or self.doneval == "Evening Snack":
            self.calorie = self.res[11]/8
            self.fat = self.res[12]/8
            self.carbs = self.res[13]/8
            self.protein = self.res[14]/8
        else:
            self.calorie = self.res[11]/4
            self.fat = self.res[12]/4
            self.carbs = self.res[13]/4
            self.protein = self.res[14]/4


    def donebtnfn(self):
        if not(self.cuisineval) or not(self.dietval) or not(self.doneval):
            messagebox.showwarning("Warning","Enter Cuisine, dietval and timezone")
        else:
            result = database.mealgenerate(self.calorie,self.fat,self.carbs,self.protein,self.cuisineval,self.dietval)
            result2 = result['results']
            title = []
            calorie = []
            fat = []
            protein = []
            carbs = []
            for i in result2:
                title.append(i['title'])
                nutrition = i['nutrition']['nutrients']
                for j in nutrition:
                    if j['name'] == 'Calories':
                        calorie.append(j['amount'])
                    elif j['name'] == 'Protein':
                        protein.append(j['amount'])
                    elif j['name'] == 'Carbohydrates':
                        carbs.append(j['amount'])
                    elif j['name'] == 'Fat':
                        fat.append(j['amount'])
            length = len(title)
            for k in range(length):
                self.dietcharlbl = Label(self.content,text=f"Dish = {title[k]}  Calories = {calorie[k]}  Protein = {protein[k]}  Fat = {fat[k]}",bg="white",font="Arial 10 bold")
                self.dietcharlbl.place(x=400,y=(100+(k*50)))


if __name__ == "__main__":
    meal_generator()