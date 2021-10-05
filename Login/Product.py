from tkinter import *
from tkinter import ttk, messagebox
# from tkinter.ttk import *
#import tkinter.messagebox as mb
from PIL import ImageTk, Image
import mysql.connector

root=Tk()

        
class Product:

    def __init__(self, root):
        
        self.root = root
        self.root.title("Login System (OSHES)")
        self.root.geometry("1280x700+200+70")
        self.root.resizable(False, False)

        #Adding image#

        self.image=ImageTk.PhotoImage(file="/Login/light5.jpg")
        self.label=Label(self.root, image=self.image)
        self.label.pack()
        
        
        #Login Frame
        self.frame = Frame(self.root, bg="#FFD1C1")
        self.frame.place(x=80, y=50, height=600, width=1100)


        #Label in Frame
        self.title = Label(self.frame, text = "Product Catalogue", font=("Calibri", 20, 'bold'), bg="#FFD1C1")
        self.title.place(x=455, y=10)

        self.light1 = ImageTk.PhotoImage(file="/Login/lights1.jpg")
        light1=Label(self.root, image=self.light1)
        self.lock1 = ImageTk.PhotoImage(file="/Login/lock1.jpg")
        lock1=Label(self.root, image=self.lock1)
        
        btn_light1 = Button(self.frame, cursor="hand2", command=self.direct_LightsView, image=self.light1, height=400, width=400)
        btn_light1.place(x=80, y=100)

        btn_lock1 = Button(self.frame, cursor="hand2", command=self.direct_SafeView, image=self.lock1, height=400, width=400)
        btn_lock1.place(x=600, y=100)

        self.lights = Label(self.frame, text = "Lights", font=("Calibri", 20, 'bold'), bg="#FFD1C1")
        self.lights.place(x=230, y=520)

        self.locks = Label(self.frame, text = "Safes", font=("Calibri", 20, 'bold'), bg="#FFD1C1")
        self.locks.place(x=770, y=520)


        
    def direct_LightsView(self):
        root.destroy()
        import LightsView

    def direct_SafeView(self):
        self.root.destroy()
        import LocksView


      
main = Product(root)
root.mainloop()
