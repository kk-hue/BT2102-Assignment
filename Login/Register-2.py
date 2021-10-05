from tkinter import *
import tkinter.messagebox as mb
from PIL import ImageTk, Image

ws = Tk()
class Register:

    def __init__(self, root):
        self.root = root
        self.root.title("Register System")
        self.root.geometry("1200x700+200+70")
        self.root.resizable(False, False)

        #Adding Image#
        self.image=ImageTk.PhotoImage(file="/Login/light2.jpg")
        self.label=Label(self.root, image=self.image)
        self.label.pack()

        #Register Frame
        self.frame = Frame(self.root, bg="#FFD1C1")
        self.frame.place(x=390, y=170, height=600, width=450)

        #Label and Boxes in Frame
        f = ('Times', 14)
        var = StringVar()
        var.set('male')

        self.name = Label(self.frame, text="Enter Name", bg='#CCCCCC',font=f)#.grid(row=0, column=0, sticky=W, pady=10)
        self.name.place(x=80, y=10)
        Label(self.frame, text="Enter Email", bg='#CCCCCC',font=f).grid(row=1, column=0, sticky=W, pady=10)
        Label(self.frame, text="Contact Number", bg='#CCCCCC',font=f).grid(row=2, column=0, sticky=W, pady=10)
        Label(self.frame, text="Select Gender", bg='#CCCCCC',font=f).grid(row=3, column=0, sticky=W, pady=10)
        Label(self.frame, text="Enter Password", bg='#CCCCCC',font=f).grid(row=5, column=0, sticky=W, pady=10)
        Label(self.frame, text="Re-Enter Password", bg='#CCCCCC',font=f).grid(row=6, column=0, sticky=W, pady=10)
        gender_frame = LabelFrame(self.frame,bg='#CCCCCC',padx=10, pady=10,)
        register_name = Entry(self.frame, font=f)
        register_email = Entry(self.frame, font=f)
        register_mobile = Entry(self.frame, font=f)
        male_rb = Radiobutton(self.frame, text='Male',bg='#CCCCCC',variable=var,value='male',font=('Times', 10),)
        female_rb = Radiobutton(self.frame,text='Female',bg='#CCCCCC',variable=var,value='female',font=('Times', 10),)
        others_rb = Radiobutton(self.frame,text='Others',bg='#CCCCCC',variable=var,value='others',font=('Times', 10))
        register_pwd = Entry(self.frame, font=f,show='*')
        pwd_again = Entry(self.frame, font=f,show='*')
        register_btn = Button(self.frame, width=15, text='Register', font=f, relief=SOLID,cursor='hand2',command=None)

        register_name.grid(row=0, column=1, pady=10, padx=20)
        register_email.grid(row=1, column=1, pady=10, padx=20) 
        register_mobile.grid(row=2, column=1, pady=10, padx=20)
        register_pwd.grid(row=5, column=1, pady=10, padx=20)
        pwd_again.grid(row=6, column=1, pady=10, padx=20)
        register_btn.grid(row=7, column=1, pady=10, padx=20)
        self.frame.pack()

        gender_frame.grid(row=3, column=1, pady=10, padx=20)
        male_rb.pack(expand=True, side=LEFT)
        female_rb.pack(expand=True, side=LEFT)
        others_rb.pack(expand=True, side=LEFT)

        check_counter=0
        warn = ""

        if register_name.get() == "":
            warn = "Name can't be empty"
        else:
            check_counter += 1

        check_counter=0
        
        if register_email.get() == "":
            warn = "Email can't be empty"
        else:
            check_counter += 1

        if register_mobile.get() == "":
           warn = "Contact can't be empty"
        else:
            check_counter += 1
    
        if  var.get() == "":
            warn = "Select Gender"
        else:
            check_counter += 1

        if register_pwd.get() == "":
            warn = "Password can't be empty"
        else:
            check_counter += 1

        if pwd_again.get() == "":
            warn = "Re-enter password can't be empty"
        else:
            check_counter += 1

        if register_pwd.get() != pwd_again.get():
            warn = "Passwords didn't match!"
        else:
           check_counter += 1

main=Register(ws)
ws.mainloop()
