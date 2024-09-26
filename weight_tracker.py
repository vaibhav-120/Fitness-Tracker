from tkinter import *
from matplotlib import pyplot
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import database
from datetime import date
from tkinter import messagebox
import pandas as pd

class WeightTracker():
    def __init__(self,content,res):
        self.res = res
        self.weightgoal = res[9]
        self.weighttime = res[10]
        self.id = res[0]
        self.content = content
        for widget in self.content.winfo_children():
            widget.destroy()

        self.weightinputlbl = Label(self.content,text="Enter your current weight")
        self.weightinputlbl.place(x=600,y=500)
        self.weightinput = Entry(self.content)
        self.weightinput.place(x=700,y=500)
        self.weightinputbtn = Button(self.content,text="ENTER",command=self.weightinputfn)
        self.weightinputbtn.place(x=850,y=500)

        fig = Figure(figsize = (10, 5),dpi = 100)
  
        data = database.fetchweight()
        x=[]
        y=[]
        counter = 0
        plot1 = fig.add_subplot(111)
        lastdate = self.weighttime*30
        plot1.set_xlabel("Day")
        plot1.set_ylabel("Weight")
        plot1.plot([1,lastdate],[self.weightgoal,self.weightgoal],linestyle='dashed')
        plot1.text((lastdate/2),self.weightgoal+0.2,'Target')
        if (len(data)) == 1:
            x.append(1)
            y.append(data[0][1])
            plot1.scatter(x,y)
        else:
            for i in data:
                counter = counter+1
                y.append(i[1])
            for j in range(counter):
                x.append(j+1)
            plot1.plot(x,y)
        
        canvas = FigureCanvasTkAgg(fig,master = self.content)  
        canvas.draw()
        canvas.get_tk_widget().place(x=0,y=0)

    def weightinputfn(self):
        weight = self.weightinput.get()
        day = date.today()
        if weight:
            try:
                weight = int(weight)
            except:
                messagebox.showwarning("Warning","Enter numeric value only")
            if type(weight) == int:
                if messagebox.askyesno("Confirmation",f"Enter {weight}KG as your current weight"):
                    database.enterweight((self.id,weight,day))
                    messagebox.showinfo("Info","Weight added successfully")
                    WeightTracker(self.content,self.res)





if __name__ == "__main__":
    WeightTracker()