from tkinter import *
from tkinter import ttk, messagebox
# from tkinter.ttk import *
#import tkinter.messagebox as mb
from PIL import ImageTk, Image
import mysql.connector

root=Tk()

def direct_light1(self):
        self.root.destroy()
        import Lights1


        
class LightsView:

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


        #Lights Image
        self.lights1 = ImageTk.PhotoImage(file="/Login/lights1.jpg")
        lights1 = Label(self.root, image=self.lights1)
        lights1.place(x=120, y=150, height=300, width=300)
        self.label.pack()
        
        self.lights2 = ImageTk.PhotoImage(file="/Login/lights2.png")
        lights2 = Label(self.root, image=self.lights2)
        lights2.place(x=480, y=150, height=300, width=300)
        self.label.pack()

        self.smartlight1 = ImageTk.PhotoImage(file="/Login/smartlight1.jpg")
        smartlight1 = Label(self.root, image=self.smartlight1)
        smartlight1.place(x=830, y=150, height=300, width=300)
        self.label.pack()
        

        #Label in Frame
        self.title = Label(self.frame, text = "Lights Catalogue", font=("Calibri", 20, 'bold'), bg="#FFD1C1")
        self.title.place(x=455, y=10)
        
        btn_light1 = Button(self.frame, cursor="hand2", command=self.direct_light1, text="Lights 1", font=("Calibri", 15, 'bold'), bg="#FFD1C1", bd=0, fg="red")
        btn_light1.place(x=150, y=450)

        btn_light2 = Button(self.frame, cursor="hand2", command=self.direct_light1, text="Lights 2", font=("Calibri", 15, 'bold'), bg="#FFD1C1", bd=0, fg="red")
        btn_light2.place(x=500, y=450)

        btn_smartlight1 = Button(self.frame, cursor="hand2", command=self.direct_light1, text="SmartHome 1", font=("Calibri", 15, 'bold'), bg="#FFD1C1", bd=0, fg="red")
        btn_smartlight1.place(x=850, y=450)

        self.backBtn = Button(self.frame, text = "Back", activebackground = "#00B0F0",
                              activeforeground="white", fg="black",
                              bg="#FFD1C1", font=("Calibri", 15, 'bold'),
                              command=self.back_Product)
        self.backBtn.place(x=920, y=20, width=100)

    def back_Product(self):
        self.root.destroy()
        import Product

    def direct_light1(self):
        self.root.destroy()
        import Lights1

    def direct_light2(self):
        self.root.destroy()
        import Lights2

    def direct_smartlight1(self):
        self.root.destroy()
        import SmartLight1

      
main = LightsView(root)
root.mainloop()
