from tkinter import *
from tkinter import ttk
import meal_tree,database

class MealTracker():
    def __init__(self,content,res):
        self.res = res
        self.content = content
        for widget in self.content.winfo_children():
            widget.destroy()
        self.perdaycalorie = res[11]
        self.perdayfat = res[12]
        self.perdaycarb = res[13]
        self.perdayprotein = res[14]

        self.bcalorie = self.perdaycalorie / 4
        self.bfat = self.perdayfat / 4
        self.bcarb = self.perdaycarb / 4
        self.bprotein = self.perdayprotein / 4

        self.mscalorie = self.bcalorie / 2
        self.msfat = self.bfat / 2
        self.mscarb = self.bcarb / 2
        self.msprotein = self.bprotein / 2

        self.lcalorie = self.bcalorie
        self.lfat = self.bfat
        self.lcarb = self.bcarb
        self.lprotein = self.bprotein

        self.escalorie = self.mscalorie
        self.esfat = self.msfat
        self.escarb = self.mscarb
        self.esprotein = self.msprotein

        self.dcalorie = self.bcalorie
        self.dfat = self.bfat
        self.dcarb = self.bcarb
        self.dprotein = self.bprotein

        self.mainheading = Label(self.content,text="Calorie Tracker",font=("Microsoft YaHei UI", 20, "bold"),bg="white")
        self.mainheading.place(x=400,y=10)

        self.breakfastlbl = Label(self.content,text="Breakfast",font="Arial 15 bold",bg="white")
        self.breakfastlbl.place(x=20,y=75)
        self.breakfastlbl2 = Label(self.content,text=f"Eat upto {self.bcalorie} calorie",bg="white",fg="green",font="Arial 10 bold")
        self.breakfastlbl2.place(x=20,y=105)
        self.breakfastlbl3 = Label(self.content,text=f"Fat = {self.bfat} gm",bg="white",fg="red",font="Arial 10 bold")
        self.breakfastlbl3.place(x=220,y=105)
        self.breakfastlbl4 = Label(self.content,text=f"Carbs = {self.bcarb} gm",bg="white",fg="blue",font="Arial 10 bold")
        self.breakfastlbl4.place(x=320,y=105)
        self.breakfastlbl5 = Label(self.content,text=f"Protein = {self.bprotein} gm",bg="white",fg="orange",font="Arial 10 bold")
        self.breakfastlbl5.place(x=470,y=105)
        self.breakCal = StringVar()
        self.breakCal.set('')
        self.breakfat = StringVar()
        self.breakfat.set('')
        self.breakcarb = StringVar()
        self.breakcarb.set('')
        self.breakprotein = StringVar()
        self.breakprotein.set('')
        self.breakfastlbl6 = Label(self.content, textvariable = self.breakCal, bg="white",font="Arial 10 bold")
        self.breakfastlbl6.place(x=20,y=125)
        self.breakfastlbl7 = Label(self.content, textvariable = self.breakfat, bg="white",font="Arial 10 bold")
        self.breakfastlbl7.place(x=220,y=125)
        self.breakfastlbl8 = Label(self.content, textvariable = self.breakcarb, bg="white",font="Arial 10 bold")
        self.breakfastlbl8.place(x=320,y=125)
        self.breakfastlbl9 = Label(self.content, textvariable = self.breakprotein, bg="white",font="Arial 10 bold")
        self.breakfastlbl9.place(x=470,y=125)
        self.baddbtn = Button(self.content,text="Add food to cart",bg="orange",fg="white",font="Arial 12 bold",command=lambda: self.treefnb(self.breakCal,self.breakfat,self.breakcarb,self.breakprotein))
        self.baddbtn.place(x=950,y=90)


        self.morningsnacklbl = Label(self.content,text="Morning Snacks",font="Arial 15 bold",bg="white")
        self.morningsnacklbl.place(x=20,y=185)
        self.morningsnacklbl2 = Label(self.content,text=f"Eat upto {self.mscalorie} calorie",bg="white",fg="green",font="Arial 10 bold")
        self.morningsnacklbl2.place(x=20,y=215)
        self.morningsnacklbl3 = Label(self.content,text=f"Fat = {self.msfat} gm",bg="white",fg="red",font="Arial 10 bold")
        self.morningsnacklbl3.place(x=220,y=215)
        self.morningsnacklbl4 = Label(self.content,text=f"Carbs = {self.mscarb} gm",bg="white",fg="blue",font="Arial 10 bold")
        self.morningsnacklbl4.place(x=320,y=215)
        self.morningsnacklbl5 = Label(self.content,text=f"Protein = {self.msprotein} gm",bg="white",fg="orange",font="Arial 10 bold")
        self.morningsnacklbl5.place(x=470,y=215)
        self.morsnackCal = StringVar()
        self.morsnackCal.set('')
        self.morsnackfat = StringVar()
        self.morsnackfat.set('')
        self.morsnackcarb = StringVar()
        self.morsnackcarb.set('')
        self.morsnackprotein = StringVar()
        self.morsnackprotein.set('')
        self.morningsnacklbl6 = Label(self.content, textvariable = self.morsnackCal, bg="white",font="Arial 10 bold")
        self.morningsnacklbl6.place(x=20,y=235)
        self.morningsnacklbl7 = Label(self.content, textvariable = self.morsnackfat, bg="white",font="Arial 10 bold")
        self.morningsnacklbl7.place(x=220,y=235)
        self.morningsnacklbl8 = Label(self.content, textvariable = self.morsnackcarb, bg="white",font="Arial 10 bold")
        self.morningsnacklbl8.place(x=320,y=235)
        self.morningsnacklbl9 = Label(self.content, textvariable = self.morsnackprotein, bg="white",font="Arial 10 bold")
        self.morningsnacklbl9.place(x=470,y=235)
        self.msaddbtn = Button(self.content,text="Add food to cart",bg="orange",fg="white",font="Arial 12 bold",command=lambda: self.treefnms(self.morsnackCal,self.morsnackfat,self.morsnackcarb,self.morsnackprotein))
        self.msaddbtn.place(x=950,y=200)

        
        self.lunchlbl = Label(self.content,text="Lunch",font="Arial 15 bold",bg="white")
        self.lunchlbl.place(x=20,y=295)
        self.lunchlbl2 = Label(self.content,text=f"Eat upto {self.lcalorie} calorie",bg="white",fg="green",font="Arial 10 bold")
        self.lunchlbl2.place(x=20,y=325)
        self.lunchlbl3 = Label(self.content,text=f"Fat = {self.lfat} gm",bg="white",fg="red",font="Arial 10 bold")
        self.lunchlbl3.place(x=220,y=325)
        self.lunchlbl4 = Label(self.content,text=f"Carbs = {self.lcarb} gm",fg="blue",bg="white",font="Arial 10 bold")
        self.lunchlbl4.place(x=320,y=325)
        self.lunchlbl5 = Label(self.content,text=f"Protein = {self.lprotein} gm",fg="orange",bg="white",font="Arial 10 bold")
        self.lunchlbl5.place(x=470,y=325)
        self.lunchCal = StringVar()
        self.lunchCal.set('')
        self.lunchfat = StringVar()
        self.lunchfat.set('')
        self.lunchcarb = StringVar()
        self.lunchcarb.set('')
        self.lunchprotein = StringVar()
        self.lunchprotein.set('')
        self.lunchlbl6 = Label(self.content, textvariable = self.lunchCal, bg="white",font="Arial 10 bold")
        self.lunchlbl6.place(x=20,y=345)
        self.lunchlbl7 = Label(self.content, textvariable = self.lunchfat, bg="white",font="Arial 10 bold")
        self.lunchlbl7.place(x=220,y=345)
        self.lunchlbl8 = Label(self.content, textvariable = self.lunchcarb, bg="white",font="Arial 10 bold")
        self.lunchlbl8.place(x=320,y=345)
        self.lunchlbl9 = Label(self.content, textvariable = self.lunchprotein, bg="white",font="Arial 10 bold")
        self.lunchlbl9.place(x=470,y=345)
        self.laddbtn = Button(self.content,text="Add food to cart",bg="orange",fg="white",font="Arial 12 bold",command=lambda: self.treefnl(self.lunchCal,self.lunchfat,self.lunchcarb,self.lunchprotein))
        self.laddbtn.place(x=950,y=310)
        
        
        self.eveningsnacklbl = Label(self.content,text="Evening Snacks",font="Arial 15 bold",bg="white")
        self.eveningsnacklbl.place(x=20,y=405)
        self.eveningsnacklbl2 = Label(self.content,text=f"Eat upto {self.escalorie} calorie",bg="white",fg="green",font="Arial 10 bold")
        self.eveningsnacklbl2.place(x=20,y=435)
        self.eveningsnacklbl3 = Label(self.content,text=f"Fat = {self.esfat} gm",fg="red",bg="white",font="Arial 10 bold")
        self.eveningsnacklbl3.place(x=220,y=435)
        self.eveningsnacklbl4 = Label(self.content,text=f"Carbs = {self.escarb} gm",fg="blue",bg="white",font="Arial 10 bold")
        self.eveningsnacklbl4.place(x=320,y=435)
        self.eveningsnacklbl5 = Label(self.content,text=f"Protein = {self.esprotein} gm",fg="orange",bg="white",font="Arial 10 bold")
        self.eveningsnacklbl5.place(x=470,y=435)
        self.evensnackCal = StringVar()
        self.evensnackCal.set('')
        self.evensnackfat = StringVar()
        self.evensnackfat.set('')
        self.evensnackcarb = StringVar()
        self.evensnackcarb.set('')
        self.evensnackprotein = StringVar()
        self.evensnackprotein.set('')
        self.eveningsnacklbl6 = Label(self.content, textvariable = self.evensnackCal, bg="white",font="Arial 10 bold")
        self.eveningsnacklbl6.place(x=20,y=455)
        self.eveningsnacklbl7 = Label(self.content, textvariable = self.evensnackfat, bg="white",font="Arial 10 bold")
        self.eveningsnacklbl7.place(x=220,y=455)
        self.eveningsnacklbl8 = Label(self.content, textvariable = self.evensnackcarb, bg="white",font="Arial 10 bold")
        self.eveningsnacklbl8.place(x=320,y=455)
        self.eveningsnacklbl9 = Label(self.content, textvariable = self.evensnackprotein, bg="white",font="Arial 10 bold")
        self.eveningsnacklbl9.place(x=470,y=455)
        self.esaddbtn = Button(self.content,text="Add food to cart",bg="orange",fg="white",font="Arial 12 bold",command=lambda: self.treefnes(self.evensnackCal,self.evensnackfat,self.evensnackcarb,self.evensnackprotein))
        self.esaddbtn.place(x=950,y=420)
        
        
        self.dinnerlbl = Label(self.content,text="Dinner",font="Arial 15 bold",bg="white")
        self.dinnerlbl.place(x=20,y=515)
        self.dinnerlbl2 = Label(self.content,text=f"Eat upto {self.dcalorie} calorie",bg="white",fg="green",font="Arial 10 bold")
        self.dinnerlbl2.place(x=20,y=545)
        self.dinnerlbl3 = Label(self.content,text=f"Fat = {self.dfat} gm",bg="white",fg="red",font="Arial 10 bold")
        self.dinnerlbl3.place(x=220,y=545)
        self.dinnerlbl4 = Label(self.content,text=f"Carbs = {self.dcarb} gm",bg="white",fg="blue",font="Arial 10 bold")
        self.dinnerlbl4.place(x=320,y=545)
        self.dinnerlbl5 = Label(self.content,text=f"Protein = {self.dprotein} gm",bg="white",fg="orange",font="Arial 10 bold")
        self.dinnerlbl5.place(x=470,y=545)
        self.dinnerCal = StringVar()
        self.dinnerCal.set('')
        self.dinnerfat = StringVar()
        self.dinnerfat.set('')
        self.dinnercarb = StringVar()
        self.dinnercarb.set('')
        self.dinnerprotein = StringVar()
        self.dinnerprotein.set('')
        self.dinnerlbl6 = Label(self.content, textvariable = self.dinnerCal, bg="white",font="Arial 10 bold")
        self.dinnerlbl6.place(x=20,y=565)
        self.dinnerlbl7 = Label(self.content, textvariable = self.dinnerfat, bg="white",font="Arial 10 bold")
        self.dinnerlbl7.place(x=220,y=565)
        self.dinnerlbl8 = Label(self.content, textvariable = self.dinnercarb, bg="white",font="Arial 10 bold")
        self.dinnerlbl8.place(x=320,y=565)
        self.dinnerlbl9 = Label(self.content, textvariable = self.dinnerprotein, bg="white",font="Arial 10 bold")
        self.dinnerlbl9.place(x=470,y=565)
        self.daddbtn = Button(self.content,text="Add food to cart",bg="orange",fg="white",font="Arial 12 bold",command=lambda: self.treefnd(self.dinnerCal,self.dinnerfat,self.dinnercarb,self.dinnerprotein))
        self.daddbtn.place(x=950,y=530)
        

    def treefnb(self,cal,fat,carb,protein):
        id = self.res[0]
        print(self.res)
        data = database.fetchfood((id,"b"))
        meal_tree.Tree("b",self.res,data,cal,fat,carb,protein)
    def treefnms(self,cal,fat,carb,protein):
        id = self.res[0]
        data = database.fetchfood((id,"ms"))
        meal_tree.Tree("ms",self.res,data,cal,fat,carb,protein)
    def treefnl(self,cal,fat,carb,protein):
        id = self.res[0]
        data = database.fetchfood((id,"l"))
        meal_tree.Tree("l",self.res,data,cal,fat,carb,protein)
    def treefnes(self,cal,fat,carb,protein):
        id = self.res[0]
        data = database.fetchfood((id,"es"))
        meal_tree.Tree("es",self.res,data,cal,fat,carb,protein)
    def treefnd(self,cal,fat,carb,protein):
        id = self.res[0]
        data = database.fetchfood((id,"d"))
        meal_tree.Tree("d",self.res,data,cal,fat,carb,protein)



if __name__ == "__main__":
    MealTracker()