from tkinter import *
from tkinter import ttk
import database
from datetime import date
from tkinter import messagebox

class Tree():
    def __init__(self,time,res,data,calvariable,fatvar,carbvar,proteinvar):
        self.fatvariable = fatvar
        self.carbvariable = carbvar
        self.proteinvariable = proteinvar
        self.res = res
        self.lblVariable = calvariable
        self.fatvar = self.res[12]
        self.carbvar = self.res[13]
        self.proteinvar = self.res[14]
        self.time = time
        self.calstore = 0
        self.fatstore = 0
        self.carbsstore = 0
        self.proteinstore = 0
        self.root = Tk()
        self.root.geometry("1000x400")
        self.root.title("Meals")
        self.value = []

        self.col = ['food','calories','fat','carbs','protein']
        self.tree = ttk.Treeview(self.root,columns=self.col,show='headings')
        self.tree.heading('food',text='Food')
        self.tree.heading('calories',text='Calories')
        self.tree.heading('fat',text='Fat')
        self.tree.heading('carbs',text='Carbs')
        self.tree.heading('protein',text='Protein')

        self.food = []

        self.tree.pack()

        if data:
            self.prevadd(data)
            data = False

        self.frame = Frame(self.root,width=1000,height=200,bg="grey")
        self.frame.place(x=0,y=225)

        self.foodlbl = Label(self.frame,text="Enter food with quantity",bg="grey",fg="white",font="Arial 12 bold")
        self.foodlbl.place(x=20,y=40)
        self.foodentry = Entry(self.frame,font="Arial 11 bold")
        self.foodentry.place(x=250,y=40)

        self.addbtn = Button(self.frame,text="Add",font="Arial 12 bold",fg="white",bg="black",command=self.add)
        self.addbtn.place(x=50,y=120)

        self.donebtn = Button(self.frame,text="Done",font="Arial 12 bold",fg="white",bg="black",command=self.done)
        self.donebtn.place(x=300,y=120)


        self.root.mainloop()

    def add(self):
        if self.foodentry.get():
            food = self.foodentry.get()
            data = database.checkfood(food)
            if data:
                self.date = date.today()
                calories = data[0][4]
                calories = float(calories[9:])
                fat = data[0][5]
                fat = float(fat[5:])
                carbs = data[0][7]
                carbs = float(carbs[6:])
                protein = data[0][10]
                protein = float(protein[8:])
                value = (self.res[0],food,calories,fat,carbs,protein,self.time,self.date)
                self.value.append(value)
                self.tree.insert('',1,values=value[1:])
                self.calstore = self.calstore + calories
                self.fatstore = self.fatstore + fat
                self.carbsstore = self.carbsstore + carbs
                self.proteinstore = self.proteinstore + protein
                try:
                    self.calorielbl.destroy()
                except:
                    pass
                self.callbl = Label(self.frame,text="Total =",font="Arial 15 bold",fg="white",bg="grey")
                self.callbl.place(x=500,y=40)
                self.calorielbl = Label(self.frame,text=(f"{self.calstore} Calories"),font="Arial 15 bold",fg="white",bg="grey")
                self.calorielbl.place(x=590,y=40)
                self.fatlbl = Label(self.frame,text=(f"{self.fatstore} gm fat"),font="Arial 15 bold",fg="white",bg="grey")
                self.fatlbl.place(x=800,y=40)
                self.carblbl = Label(self.frame,text=(f"{self.carbsstore} gm carbs"),font="Arial 15 bold",fg="white",bg="grey")
                self.carblbl.place(x=590,y=70)
                self.proteinlbl = Label(self.frame,text=(f"{self.proteinstore} gm protein"),font="Arial 15 bold",fg="white",bg="grey")
                self.proteinlbl.place(x=800,y=70)
                self.lblVariable.set(f'Consumed upto {self.calstore} calories')
                self.fatvariable.set(f'Fat = {self.fatstore} gm')
                self.carbvariable.set(f'Carbs = {self.carbsstore} gm')
                self.proteinvariable.set(f'Protein = {self.proteinstore} gm')
            else:
                messagebox.showinfo("Meal Info","Food item that you entered is not in list")
                self.root.destroy()


    def prevadd(self,data):
        for i in data:
            food = i[1]
            calories = i[2]
            fat = i[3]
            carbs = i[4]
            protein = i[5]
            self.calstore += calories
            self.fatstore += fat
            self.carbsstore += carbs
            self.proteinstore += protein

            value = (food,calories,fat,carbs,protein)
            self.tree.insert('',1,values=value)



    def done(self):
        res = database.enterfood(self.value)
        if not res:
            messagebox.showerror("Error","Something went wrong")
        else:
            self.root.destroy()



if __name__ == "__main__":
    Tree()