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
        
class LocksView:

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
        self.lock1 = ImageTk.PhotoImage(file="/Login/lock11.jpg")
        lock1 = Label(self.root, image=self.lock1)
        lock1.place(x=120, y=150, height=280, width=220)
        self.label.pack()
        
        self.lock2 = ImageTk.PhotoImage(file="/Login/lock22.jpg")
        lock2 = Label(self.root, image=self.lock2)
        lock2.place(x=380, y=150, height=280, width=220)
        self.label.pack()

        self.lock3 = ImageTk.PhotoImage(file="/Login/lock33.jpg")
        lock3 = Label(self.root, image=self.lock3)
        lock3.place(x=660, y=150, height=280, width=220)
        self.label.pack()

        self.smartlock1 = ImageTk.PhotoImage(file="/Login/smartlock11.jpg")
        smartlock1 = Label(self.root, image=self.smartlock1)
        smartlock1.place(x=920, y=150, height=280, width=220)
        self.label.pack()
        

        #Label in Frame
        self.title = Label(self.frame, text = "Locks Catalogue", font=("Calibri", 20, 'bold'), bg="#FFD1C1")
        self.title.place(x=455, y=10)
        
        btn_lock1 = Button(self.frame, cursor="hand2", command=self.direct_lock1, text="Safe 1", font=("Calibri", 15, 'bold'), bg="#FFD1C1", bd=0, fg="red")
        btn_lock1.place(x=120, y=400)

        btn_lock2 = Button(self.frame, cursor="hand2", command=self.direct_lock2, text="Safe 2", font=("Calibri", 15, 'bold'), bg="#FFD1C1", bd=0, fg="red")
        btn_lock2.place(x=370, y=400)

        btn_lock3 = Button(self.frame, cursor="hand2", command=self.direct_lock3, text="Safe 3", font=("Calibri", 15, 'bold'), bg="#FFD1C1", bd=0, fg="red")
        btn_lock3.place(x=650, y=400)

        btn_smartlock1 = Button(self.frame, cursor="hand2", command=self.direct_smartlock1, text="SmartHome 1", font=("Calibri", 15, 'bold'), bg="#FFD1C1", bd=0, fg="red")
        btn_smartlock1.place(x=880, y=400)

        self.backBtn = Button(self.frame, text = "Back", activebackground = "#00B0F0",
                                  activeforeground="white", fg="black",
                                  bg="#FFD1C1", font=("Calibri", 15, 'bold'), command=self.back)
        self.backBtn.place(x=920, y=20, width=100)
        
    def back(self):
        self.root.destroy()
        import Product

    def direct_lock1(self):
        self.root.destroy()
        import Safe1

    def direct_lock2(self):
        self.root.destroy()
        import Safe2

    def direct_lock3(self):
        self.root.destroy()
        import Safe3

    def direct_smartlock1(self):
        self.root.destroy()
        import SmartSafe1





      
main = LocksView(root)
root.mainloop()
