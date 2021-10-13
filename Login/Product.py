from tkinter import *
from tkinter import ttk, messagebox
# from tkinter.ttk import *
# import tkinter.messagebox as mb
from PIL import ImageTk, Image
import mysql.connector
from LightsView import LightView
from LocksView import LocksView

class Product:

    def __init__(self, root):
        self.root = root
        self.root.title("Products (OSHES)")
        self.root.geometry("1280x700+200+70")
        self.root.resizable(False, False)

        # Adding image#

        self.image = ImageTk.PhotoImage(file="/Login/bg2.jpg")
        self.label = Label(self.root, image=self.image)
        self.label.pack()

        # Login Frame
        self.frame = Frame(self.root, bg="#FFD1C1")
        self.frame.place(x=80, y=50, height=600, width=1100)

        # Label in Frame
        self.title = Label(self.frame, text="Product Catalogue", font=("Arial Narrow", 20, 'bold', "underline"), bg="#FFD1C1")
        self.title.place(x=445, y=5)

        self.desc = Label(self.frame, text="Welcome to OSHES, where you can find the best lights and locks in town. \n "
                                           "Browse our latest products and purchase them through our online system",
                          font=("Cambria", 15), bg="#FFD1C1")
        self.desc.place(x=230, y=40)

        self.light1 = ImageTk.PhotoImage(file="/Login/prolight1.jpg")
        light1 = Label(self.root, image=self.light1)
        self.lock1 = ImageTk.PhotoImage(file="/Login/prolocks1.jpg")
        lock1 = Label(self.root, image=self.lock1)

        btn_light1 = Button(self.frame, cursor="hand2", image=self.light1, height=400, width=400,
                            command=self.lightsview)
        btn_light1.place(x=80, y=120)

        btn_lock1 = Button(self.frame, cursor="hand2", image=self.lock1, height=400, width=400,
                           command=self.locksview)
        btn_lock1.place(x=600, y=120)

        self.lights = Label(self.frame, text="Lights", font=("Calibri", 20, 'bold'), bg="#FFD1C1")
        self.lights.place(x=230, y=540)

        self.locks = Label(self.frame, text="Safes", font=("Calibri", 20, 'bold'), bg="#FFD1C1")
        self.locks.place(x=770, y=540)

    def lightsview(self):
        self.new_win = Toplevel(self.root)
        self.new_Obj = LightView(self.new_win)

    def locksview(self):
        self.new_win = Toplevel(self.root)
        self.new_Obj = LocksView(self.new_win)


if __name__ =="__main__":
    root=Tk()
    main = Product(root)
    root.mainloop()
