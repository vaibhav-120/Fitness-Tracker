from tkinter import *
from PIL import Image,ImageTk
import webbrowser


class ExerciseDetails():
    def __init__(self,content,res,exercise,exercisevideo):
        self.res = res
        self.content = Frame(content,width=850,height=540,bg="white")
        self.content.place(x=10,y=50)

        self.videoimg = Image.open("images/videologo.png").resize((20,20))
        self.videoimgtk = ImageTk.PhotoImage(self.videoimg)
        for j in range(4):
            for i in range(4):
                self.item = Frame(self.content,width=205,height=100,bg="#38354a")
                self.item.place(x=((j*200)+(j*10)),y=((i*100)+(28*i)+28))

                self.exlbl = Label(self.item,text=exercise[(j*4)+i],font="Arial 10 bold",bg="#38354a",fg="white",wraplength=170)
                self.exlbl.place(x=10,y=10)

                self.btn = Button(self.item,text="Watch",image=self.videoimgtk,compound=LEFT,command= lambda url = exercisevideo[(j*4)+i]:self.exercisevideofn(url))
                self.btn.place(x=130,y=60)

    def exercisevideofn(self,url):
        webbrowser.open(url)