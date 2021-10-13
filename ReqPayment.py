from tkinter import *
from tkinter import messagebox
import tkinter.ttk
from PaymentPage import Payment_Page
import mysql.connector
from datetime import datetime
from datetime import timedelta, date
from tkinter import messagebox
from datetime import date




class Request_Payment:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1320x700+0+0")
        self.root.title("Billing Software")
        bg_color = "black"
        title = Label(self.root, text="REQUEST SUBMISSION & PAYMENT", bd=15, bg="black", fg="white",
                      font=("times new roman", 30, "bold"), pady=2).pack(fill=X)

        # ================Variables==========================
        self.flatFee = IntVar()
        self.materialFee = IntVar()
        self.amtPayable = IntVar()
        self.requestStatus = StringVar()
        self.serviceStatus = StringVar()
        self.customerID = StringVar()
        self.purchaseDateWarranty = StringVar()

        # ================Cutomers==================================

        self.itemID = StringVar()
        self.productName = StringVar()
        self.warrantyTill = datetime.now()
        self.bill_no = StringVar()
        self.search_bill = StringVar()
        self.address = StringVar()
        self.requestApprovalDate = StringVar()
        self.requestID = StringVar()
        self.purchaseDate = StringVar()
        self.date1 = datetime.now()
        self.colour = StringVar()
        self.category = StringVar()
        self.paymentID = StringVar()
        self.productID = StringVar()


        f = open("store_itemID.txt", "r")
        profile_details = []
        for line in f:
            profile_details.append(line.rstrip())
        self.customerID.set(profile_details[9])
        self.itemID.set(profile_details[0])
        self.purchaseDate.set(profile_details[10])
        self.category.set(profile_details[8])
        self.colour.set(profile_details[4])
        self.serviceStatus.set(profile_details[6])


        #GET DATA FROM REQUEST THAT HAS BEEN MADE (UPDATES REQUESTSTATUS AND REQUESTID)
        #IF REQUEST DOES NOT EXIST, CLOSE TERMINAL
        con = mysql.connector.connect(host="localhost", user="root", password="123456", database="oshes")
        cur = con.cursor()
        cur.execute("select * from Request where itemID = %s", (self.itemID.get(),))
        row = cur.fetchall()
        try:
            print("CHECKING FOR REQUEST")
            self.requestStatus.set(row[0][1])
            self.requestID.set(row[0][0])
        except:
            con.commit()
            con.close()

        # GET DATA FROM SERVICEFEE THAT HAS BEEN MADE (UPDATES SERVICE APPROVAL DATE AND PAYMENTID )
        # #IF SERVICEfee DOES NOT EXIST, CLOSE TERMINAL
        con = mysql.connector.connect(host="localhost", user="root", password="123456", database="oshes")
        cur = con.cursor()
        cur.execute("select * from servicefee where requestID = %s", (self.requestID.get(),))
        row2 = cur.fetchall()
        try:
            print("CHECKING FOR SERVICEFEE")
            self.paymentID.set(row2[0][1])
        except:
            con.commit()
            con.close()

        # GET DATA FROM payment THAT HAS BEEN MADE (UPDATES requestapprovaldate )
        # #IF payment DOES NOT EXIST, CLOSE TERMINAL
        con = mysql.connector.connect(host="localhost", user="root", password="123456", database="oshes")
        cur = con.cursor()
        cur.execute("select * from payment where paymentID = %s", (self.paymentID.get(),))
        row3 = cur.fetchall()
        try:
            self.requestApprovalDate.set(row3[0][1])
        except:
            con.commit()
            con.close()

        # GET DATA FROM ITEM (UPDATES SERVICE STATUS )
        con = mysql.connector.connect(host="localhost", user="root", password="123456", database="oshes")
        cur = con.cursor()
        cur.execute("select * from item where itemID = %s", (self.itemID.get(),))
        row3 = cur.fetchall()
        print("CHECKING FOR SERVICESTATUS")
        if row3[0][6] == None:
            self.serviceStatus.set("")
        con.commit()
        con.close()

        # GET DATA FROM ITEM PRODUCT (UPDATES PRODUCTID AND COST OF PRODUCT)
        con = mysql.connector.connect(host="localhost", user="root", password="123456", database="oshes")
        cur = con.cursor()
        cur.execute("select productID from item where itemID = %s", (self.itemID.get(),))
        row4 = cur.fetchone()
        #get productID

        self.productID.set(row4[0])
        print(self.productID.get())

        cur.execute("select cost from product where productID = %s", (self.productID.get(),))
        row5 = cur.fetchone()
        # get price
        print(row5)

        # UPDATES WARRANTYTILL
        self.warrantyTill = datetime.strptime(self.purchaseDate.get(), '%m/%d/%Y').date()
        self.warrantyTill = self.warrantyTill + timedelta(days=180)
        self.purchaseDateWarranty.set(self.warrantyTill.strftime('%d/%m/%Y'))

        print("date.compare")
        print(date.today() < self.warrantyTill)

        if self.requestStatus.get() == "Approved" and date.today() > self.warrantyTill:
            self.flatFee.set(40)
            self.materialFee.set(int(row5[0]) * 0.2)
            self.amtPayable.set(40 + float(self.materialFee.get()))
        else:
            self.flatFee.set(0)
            self.materialFee.set(0)
            self.amtPayable.set(0)

        con.commit()
        con.close()



        # =============Customer Details Frame====================
        F1 = LabelFrame(self.root, bd=8, text="Item Details", font=("times new roman", 25, "bold"), fg="white",
                        bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)

        cname_lbl = Label(F1, text="Item ID", bg=bg_color, fg="White", font=("times new roman", 15, "bold")).grid(
            row=0, column=0, padx=0, pady=0)
        cname_txt = Entry(F1, width=15, textvariable=self.itemID, font="arial 12", bd=7, relief=SUNKEN, state= "readonly").grid(row=0,
                                                                                                             column=1,
                                                                                                             pady=0,
                                                                                                             padx=3)

        cphn_lbl = Label(F1, text="Warranty Till:", bg=bg_color, fg="White", font=("times new roman", 15, "bold")).grid(
            row=0, column=2, padx=0, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.purchaseDateWarranty, font="arial 12", bd=7, relief=SUNKEN, state= "readonly").grid(row=0,
                                                                                                            column=3,
                                                                                                            pady=5,
                                                                                                            padx=3)

        c_bill_lbl = Label(F1, text="Request\nStatus", bg=bg_color, fg="White", font=("times new roman", 15, "bold")).grid(
            row=0, column=4, padx=0, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.requestStatus, font="arial 12", bd=7, relief=SUNKEN, state= "readonly").grid(
            row=0, column=5, pady=5, padx=8)


        requeststatus = Label(F1, text="Request\nApproval Date", bg=bg_color, fg="White", font=("times new roman", 15, "bold")).grid(
            row=0, column=7, padx=0, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.requestApprovalDate, font="arial 12", bd=7, relief=SUNKEN, state= "readonly").grid(
            row=0, column=8, pady=5, padx=8)

        requeststatus = Label(F1, text="Service\nStatus", bg=bg_color, fg="White", font=("times new roman", 15, "bold")).grid(
            row=0, column=9, padx=0, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.serviceStatus, font="arial 12", bd=7, relief=SUNKEN, state= "readonly").grid(
            row=0, column=10, pady=5, padx=3)


        # ===========Item Details=========
        bg_color2 = "white"

        F2 = LabelFrame(self.root, bd=20, text="Additional Item Details", font=("times new roman", 25, "bold"), fg="black", bg="white")
        F2.place(x=5, y=180, width=500, height=380)

        makereq = Button(F2, text="Make Request", command=self.make_request, bg="cadetblue", fg="white", pady=15, bd=4,
                          width=5, font="arial 14 bold").place(x=125, y=230, width=200, height=40)

        cancelreq = Button(F2, text="Cancel Request", command=self.cancel_request, bg="cadetblue", fg="white", pady=15, bd=4,
                         width=5, font="arial 14 bold").place(x=125, y=270, width=200, height=40)


        light1_lbl = Label(F2, text="Category", font=("times new roman", 16, "bold"), bg=bg_color2,
                               fg=bg_color).place(x=15, y=30, width=100, height=40)
        light1_entry = Entry(F2, width=15, textvariable=self.category, font="arial 12", bd=7, relief=SUNKEN, state="readonly").place(x=120, y=30, width=120, height=40)

        light2_lbl = Label(F2, text="Colour", font=("times new roman", 16, "bold"), bg=bg_color2,
                           fg=bg_color).place(x=15, y=80, width=80, height=40)
        light2_entry = Entry(F2, width=15, textvariable=self.colour, font="arial 12", bd=7, relief=SUNKEN, state="readonly").place(x=120, y=80, width=120, height=40)

        light1_lbl = Label(F2, text="Request ID", font=("times new roman", 16, "bold"), bg=bg_color2,
                           fg=bg_color).place(x=15, y=130, width=110, height=40)
        light1_entry = Entry(F2, width=10, textvariable=self.requestID, font=("times new roman", 14, "bold"), bd=5, state="readonly"
                            ).place(x=120, y=130, width=120, height=40)

        safe2_lbl = Label(F2, text="Please give us 5 working days to process your request.\nCome back again to this page for an update.",
                          font=("times new roman", 12, "bold"), bg="white",
                          fg="red").place(x=30, y=190, width=400, height=40)

        # ============SAFE CATEGORY===========
        bg_color2 = "white"

        F3 = LabelFrame(self.root, bd=20, text="Request Details", font=("times new roman", 25, "bold"), fg="black", bg="white")
        F3.place(x=480, y=180, width=500, height=380)


        bath_lbl = Label(F3, text="Amount\nPayable ($)", font=("times new roman", 17, "bold"), bg="WHITE",
                         fg="red").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        safe1_entry = Entry(F3, width=10, textvariable=self.amtPayable, font=("times new roman", 14, "bold"), bd=5,
                            relief=SUNKEN, state="readonly").place(x=190, y=30, width=80, height=40)

        safe1_lbl = Label(F3, text="Flat Fee", font=("times new roman", 16, "bold"), bg=bg_color2,
                               fg=bg_color).grid(row=1, column=0, padx=10, pady=10, sticky="e")
        safe1_entry = Entry(F3, width=10, textvariable=self.flatFee, font=("times new roman", 14, "bold"), bd=5,
                               relief=SUNKEN, state="readonly").place(x=190, y=80, width=80, height=40)
        safe1_txt = Label(F3, width=10, text="$40", font=("times new roman", 14, "bold"),
                               ).place(x=310, y=80, width=100, height=40)

        safe2_lbl = Label(F3, text="Material Fee", font=("times new roman", 16, "bold"), bg=bg_color2,
                           fg=bg_color).grid(row=2, column=0, padx=10, pady=10, sticky="e")
        safe2_entry = Entry(F3, width=10, textvariable=self.materialFee, font=("times new roman", 14, "bold"), bd=5,
                           relief=SUNKEN,state="readonly").place(x=190, y=130, width=80, height=40)
        safe2_txt = Label(F3, width=10, text="20% of\nItem Cost", font=("times new roman", 14, "bold")
                               ).place(x=310, y=130, width=130, height=40)

        safe2_lbl = Label(F3, text="Please make payment within\n10 days of request approval date.", font=("times new roman", 12, "bold"), bg="orange",
                          fg=bg_color).place(x=100, y=190, width=280, height=40)

        paymentID = Entry(F3, width=10, textvariable=self.paymentID, font=("times new roman", 14, "bold"), bd=5,
                            relief=SUNKEN, state="readonly").place(x=140, y=230, width=200, height=40)
        makereq = Button(F3, text="Make Payment", command=self.make_payment, bg="cadetblue", fg="white", pady=15, bd=4,
                         width=5, font="arial 14 bold").place(x=140, y=270, width=200, height=40)



        # ===============Bill Area=============
        F5 = Frame(self.root, bd=8, relief=GROOVE)
        F5.place(x=980, y=180, width=340, height=380)

        # ==============Button Frame=============

        F6 = LabelFrame(self.root, bd=8, text="", font=("times new roman", 20, "bold"), fg="black", bg="white")
        F6.place(x=0, y=560, relwidth=1, height=140)
        m1_lbl = Label(F6, text="Thank you and have a nice day ahead!", bg="white", fg="black",
                       font=("times new roman", 25, "bold")).place(x=350, y=20, width=600, height=80)

        btn_F = Frame(F6, bd=7, relief=GROOVE)
        btn_F.place(x=1200,y=15, height=102)

        Exit_btn = Button(btn_F, text="Back", command=self.Exit_app, bg="cadetblue", fg="white", pady=15, bd=4,
                          width=5, font="arial 14 bold").grid(row=0, column=0, padx=4, pady=5)

        F6 = Frame(self.root, bd=8, relief=GROOVE)
        F6.place(x=980, y=180, width=340, height=380)
        specialmsg = Label(F6, text="special\nmessage", bg="white", fg="black",
                      font=("times new roman", 25, "bold")).place(x=0, y=0, width=300, height=300)


    def Exit_app(self):
        self.root.destroy()

    def make_request(self):
        con = mysql.connector.connect(host="localhost", user="root", password="123456", database="oshes")
        cur = con.cursor()
        if self.requestStatus.get() == "Canceled":
            makeanotherreq = messagebox.askyesno("Confirmation", "Do you really want to make another request?")
            #find old request and update the request
            cur.execute("UPDATE request SET requestStatus = 'Submitted' WHERE requestID = %s", (self.itemID.get(),))
            self.requestID.set(self.itemID.get())
            self.requestStatus.set("Submitted")
            self.requestApprovalDate.set("")
            self.serviceStatus.set("Not Applicable")
            messagebox.showinfo("Notice",
                                "Your previous has been submitted.\nPlease refer to the Request ID for any queries related to this request")

        #if there is already a request ongoing
        elif self.requestStatus.get() != "" and self.requestStatus.get() != "Canceled":
            messagebox.showerror("Title", "Your previous request is still in process.")

        #if request does not exist, create request
        else:
            self.requestID.set(self.itemID.get())

            cur.execute("INSERT INTO Request VALUES (%s, 'Submitted', %s, %s, 'NatAdmin', %s)", (self.itemID.get(), str(date.today()), self.customerID.get() , self.itemID.get()))

            cur.execute("INSERT INTO servicefee VALUES (%s, 'Not Paid Yet', %s, %s, %s)", (self.requestID.get(), str(date.today()), self.flatFee.get(), self.materialFee.get()))

            self.requestStatus.set("Submitted")
            self.requestApprovalDate.set("")
            self.serviceStatus.set("Not Applicable")
            messagebox.showinfo("Notice", "Your previous has been submitted.\nPlease refer to the Request ID for any queries related to this request")
        con.commit()
        con.close()


    def cancel_request(self):
        con = mysql.connector.connect(host="localhost", user="root", password="123456", database="oshes")
        cur = con.cursor()
        if self.requestStatus.get() != "":
            answer = messagebox.askyesno("Confirmation", "Do you really want to cancel your request?")
            if answer > 0:
                cur.execute("UPDATE request SET requestStatus = 'Canceled' WHERE itemID = %s", (self.itemID.get(),))
                con.commit()
                con.close()
                self.requestStatus.set("")
                self.requestID.set("")
                self.serviceStatus.set("")
                self.requestApprovalDate.set("")
        else:
            messagebox.showerror("Error", "There is no request to cancel")
            con.commit()
            con.close()

#6month warranty

    def make_payment(self):
        con = mysql.connector.connect(host="localhost", user="root", password="123456", database="oshes")
        cur = con.cursor()
        cur.execute("select itemID,customerID,administratorID from item where itemID =%s", (self.itemID.get(),))
        row = cur.fetchall()
        print(row)
        rowholder = []
        for element in row[0]:
            rowholder.append(element)
        rowholder.append(self.amtPayable.get())
        rowholder.append(self.requestID.get())
        print("HERE")
        print(rowholder)
        if self.requestStatus.get() != "Approved":
            messagebox.showinfo("Notice", "Your request has not been approved.")
        else:
            q = open("store_custanditemID", "w")
            for t in rowholder:
                print(t)
                if t == None:
                    q.write("NULL" + "\n")
                else:
                    try:
                        q.write(''.join(str(s) for s in t.strftime("%m/%d/%Y")) + "\n")
                    except:
                        q.write(''.join(str(s) for s in t) + "\n")
            q.close()

            self.new_window = Toplevel(self.root)
            self.new_object = Payment_Page(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = Request_Payment(root)
    root.mainloop()