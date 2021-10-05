from tkinter import *
from tkinter import ttk, messagebox
# from tkinter.ttk import *
#import tkinter.messagebox as mb
from PIL import ImageTk, Image
import mysql.connector

root=Tk()

def toRegister():
    root.destroy()
    import Register3
    
        
class Login:

    def __init__(self, root):
        
        self.root = root
        self.root.title("Login System (OSHES)")
        self.root.geometry("1280x700+200+70")
        self.root.resizable(False, False)

        #Adding image#

        self.image=ImageTk.PhotoImage(file="/Login/log1.png")
        self.label=Label(self.root, image=self.image)

        self.top = ImageTk.PhotoImage(file="/Login/pro2.png")
        top = Label(self.root, image=self.top)
        top.place(x=550, y=10, height=150, width=150)
        self.label.pack()
        
        
        #Login Frame

        
        self.frame1 = Frame(self.root, bg="black")
        self.frame1.place(x=375, y=140, height=420, width=480)
        
        self.frame = Frame(self.root, bg="#FFD1C1")
        self.frame.place(x=390, y=150, height=400, width=450)


        #Label and Boxes in Frame
        self.title = Label(self.frame, text = "Login System to OSHES", font=("Calibri", 20, 'bold', "underline"), bg = "#FFD1C1")
        self.title.place(x=100, y=10)
        
        self.userlabel = Label(self.frame, text = "USER ID", font=("Calibri", 15, 'bold'), bg="#FFD1C1")
        self.userlabel.place(x=80, y=70)

        self.entry1= Entry(self.frame, font=("times new roman", 15, 'bold'))
        self.entry1.place(x=80, y=100, width=250)

        self.passlabel = Label(self.frame, text = "PASSWORD", font=("Calibri", 15, 'bold'), bg="#FFD1C1")
        self.passlabel.place(x=80, y=170)

        self.entry2= Entry(self.frame, show="*", font=("times new roman", 15, 'bold'))
        self.entry2.place(x=80, y=200, width=250)

        self.loginButton = Button(self.frame, text = "Login", activebackground = "#00B0F0",
                                  activeforeground="white", fg="white",
                                  bg="orange", font=("Calibri", 15, 'bold'), command=self.loginOSHES)
        self.loginButton.place(x=80, y=250, width=150)


        self.regButton = Button(self.frame, text = "Register", activebackground = "#00B0F0",
                                activeforeground="white", fg="white", bg="orange",
                                font=("Calibri", 15, 'bold'), command=toRegister)
        self.regButton.place(x=80, y=300, width=150)

        btn_admin = Button(self.frame, cursor="hand2", command=self.adminLogin, text="Admin Login", font=("Calibri", 12, "underline"), bg="#FFD1C1", bd=0, fg="red")
        btn_admin.place(x=50, y=350, width=150)

        
    def loginOSHES(self):
        if (self.entry1.get() == "" or self.entry2.get() == "") :
            messagebox.showerror("Error", "Please enter your Username or Password", parent=self.root)
        else:
            try:
                con=mysql.connector.connect(host="localhost", user="root", password="s63127734", database="oshes")
                cur=con.cursor()
                cur.execute("select * from Customer where customerID =%s and password = %s", (self.entry1.get(), self.entry2.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Username & Password", parent=self.root)
                else:
                    messagebox.showinfo("Success", "Welcome to OSHES", parent=self.root)
                    self.root.destroy()
                    import Product
                #con.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)

    def adminLogin(self):
        self.root.destroy()
        import AdminLogin

    #Forget Password: https://www.youtube.com/watch?v=2xzzLoDV0XY&list=PL4P8sY6zvjk6p9u8T2etiQm6EE_15QF0y&index=6&ab_channel=Webcode
                
    

main = Login(root)
root.mainloop()


        
