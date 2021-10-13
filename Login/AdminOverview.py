from tkinter import *
from tkinter import ttk, messagebox
# from tkinter.ttk import *
#import tkinter.messagebox as mb
from PIL import ImageTk, Image
import mysql.connector
from AdminSearchProduct import AdminSearchProduct
from AdminSearchItem import AdminSearchItem
from RequestManagement import RequestManagement
from ServiceManagement import ServiceManagement
from AdminUnpaid import AdminSearchCustomers

class AdminOverview:

    def __init__(self, root):

        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Admin Dashboard Overview")
        self.root.config(bg="white")
        self.root.resizable(False, False)

        #title
        title = Label(self.root, text="Admin Dashboard Overview",
                      font=("Times New Roman", 40, "bold"), bg="#010c48", fg="white",
                      anchor="w", compound="left",padx=20)
        title.place(x=0,y=0,relwidth=1,height=70)

        #Button Log Out
        btn_logout = Button(self.root, text="Logout", font=("Times New Roman", 15, "bold"),
                          bg="yellow")
        btn_logout.place(x=1100, y=10, width=150, height=50)

        #Left Menu
        leftmenu=Frame(self.root, bd=2, relief=RIDGE,bg="white")
        leftmenu.place(x=0,y=102,width=200,height=565)

        lbl_menu=Label(leftmenu, text="Menu", font=("Times New Roman", 15, "bold"), bg="#009688")
        lbl_menu.pack(side=TOP, fill=X)

        btn_product=Button(leftmenu, text="Product", command=self.product, font=("Times New Roman", 20, "bold"),bg="white",bd=3,cursor="hand2")
        btn_product.pack(side=TOP,fill=X)

        btn_item = Button(leftmenu, text="Item", command=self.item, font=("Times New Roman", 20, "bold"), bg="white", bd=3,
                             cursor="hand2")
        btn_item.pack(side=TOP, fill=X)

        btn_request = Button(leftmenu, text="Request", font=("Times New Roman", 20, "bold"), bg="white", bd=3,
                             cursor="hand2", command=self.request)
        btn_request.pack(side=TOP, fill=X)

        btn_customer = Button(leftmenu, text="Customer", font=("Times New Roman", 20, "bold"), bg="white", bd=3,
                             cursor="hand2", command=self.unpaid)
        btn_customer.pack(side=TOP, fill=X)

        btn_Service= Button(leftmenu, text="Service", font=("Times New Roman", 20, "bold"), bg="white", bd=3,
                              cursor="hand2", command=self.service)
        btn_Service.pack(side=TOP, fill=X)


        #Content

        self.lbl_product=Label(self.root,text="Total Product\n[ 7 ]", bg="#607d8b", fg="white",
                               font=("goudy old style", 20, "bold"), bd=5)
        self.lbl_product.place(x=400,y=200, height=150,width=300)

        self.lbl_item = Label(self.root, text="Total Item\n[ 2001 ]", bg="#ff5722", fg="white",
                                 font=("goudy old style", 20, "bold"), bd=5)
        self.lbl_item.place(x=850, y=200, height=150, width=300)

        self.lbl_request = Label(self.root, text="Total Request\n[ 0 ]", bg="#009688", fg="white",
                                 font=("goudy old style", 20, "bold"), bd=5)
        self.lbl_request.place(x=400, y=400, height=150, width=300)

        self.lbl_customer = Label(self.root, text="Total Customer\n[ 0 ]", bg="#ffc107", fg="white",
                                 font=("goudy old style", 20, "bold"), bd=5)
        self.lbl_customer.place(x=850, y=400, height=150, width=300)
#=============================================================================

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=AdminSearchProduct(self.new_win)

    def request(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=RequestManagement(self.new_win)

    def service(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ServiceManagement(self.new_win)

    def item(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=AdminSearchItem(self.new_win)

    def unpaid(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=AdminSearchProduct(self.new_win)

if __name__ =="__main__":
    root=Tk()
    main = AdminOverview(root)
    root.mainloop()



