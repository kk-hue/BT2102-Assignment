from tkinter import *
from tkinter import ttk, messagebox
# from tkinter.ttk import *
#import tkinter.messagebox as mb
from PIL import ImageTk, Image
import json
import mysql.connector

root=Tk()

class ItemImport:

    def __init__(self, root):

        self.root = root
        self.root.title("Item Import System")
        self.root.geometry("1350x700+0+0")
        self.root.resizable(False, False)

        title = Label(self.root, text="Item Import System", font=("calibri", 40, "bold"), bg="light blue", fg="white")
        title.pack(side=TOP, fill=X)

        # Import Frame

        self.frame1 = Frame(self.root, bg="black")
        self.frame1.place(x=375, y=140, height=520, width=480)

        self.frame = Frame(self.root, bg="light blue")
        self.frame.place(x=390, y=150, height=500, width=450)

        #Label and Boxes in Frame
        self.title = Label(self.frame, text = "Item Import System", font=("Calibri", 20, 'bold', "underline"), bg = "light blue")
        self.title.place(x=100, y=10)

        self.directorylabel = Label(self.frame, text = "JSON File Directory", font=("Calibri", 15, 'bold'), bg="light blue")
        self.directorylabel.place(x=80, y=70)

        self.directory = Entry(self.frame, font=("times new roman", 15, 'bold'))
        self.directory.place(x=80, y=100, width=250)

        self.serverlabel = Label(self.frame, text="SERVER INFORMATION", font=("Calibri", 15, 'bold'),
                                    bg="light blue")
        self.serverlabel.place(x=80, y=150, width=250)

        self.hostlabel = Label(self.frame, text = "HOST", font=("Calibri", 15, 'bold'), bg="light blue")
        self.hostlabel.place(x=80, y=180)

        self.host = Entry(self.frame, font=("times new roman", 15, 'bold'))
        self.host.place(x=80, y=210, width=250)

        self.databaselabel = Label(self.frame, text = "DATABASE", font=("Calibri", 15, 'bold'), bg="light blue")
        self.databaselabel.place(x=80, y=240)

        self.database = Entry(self.frame, font=("times new roman", 15, 'bold'))
        self.database.place(x=80, y=270, width=250)

        self.userlabel = Label(self.frame, text="USER", font=("Calibri", 15, 'bold'), bg="light blue")
        self.userlabel.place(x=80, y=300)

        self.user = Entry(self.frame, font=("times new roman", 15, 'bold'))
        self.user.place(x=80, y=330, width=250)

        self.passwordlabel = Label(self.frame, text="PASSWORD", font=("Calibri", 15, 'bold'), bg="light blue")
        self.passwordlabel.place(x=80, y=360)

        self.password = Entry(self.frame, font=("times new roman", 15, 'bold'))
        self.password.place(x=80, y=390, width=250)

        self.importButton = Button(self.frame, text="Import", activebackground="#00B0F0",
                                  activeforeground="white", fg="white",
                                  bg="crimson", font=("Calibri", 15, 'bold'), command=self.importItem)
        self.importButton.place(x=150, y=430, width=150)

    def importItem(self):
        if (self.directory.get() == "" ) :
            messagebox.showerror("Error", "Please enter the directory of your JSON file", parent=self.root)
        elif (self.host.get() == "") :
            messagebox.showerror("Error", "Please enter the host of your server", parent=self.root)
        elif (self.database.get() == "") :
            messagebox.showerror("Error", "Please enter the database of your server", parent=self.root)
        elif (self.user.get() == "") :
            messagebox.showerror("Error", "Please enter the user of your server", parent=self.root)
        elif (self.password.get() == "") :
            messagebox.showerror("Error", "Please enter the password of your server", parent=self.root)
        else:
            try:
                with open(self.directory.get()) as file:
                    data = json.load(file)
                connection = mysql.connector.connect(host=self.host.get(),
                                                     database=self.database.get(),
                                                     user=self.user.get(),
                                                     password=self.password.get())

                productList = self.product_list()
                productDict = dict()
                for product in productList:
                    productDict[(product[0], product[1])] = product[2]

                mySql_insert_query = """INSERT INTO Item
                                       VALUES (%s, %s, %s, %s, %s, %s, NULL, NULL, %s, NULL, NULL) """

                records_to_insert = [(data[0]['ItemID'], data[0]['PurchaseStatus'], data[0]['Factory'],
                                      data[0]['ProductionYear'], data[0]['Color'],
                                      data[0]['PowerSupply'], productDict[(data[0]['Category'], data[0]['Model'])])]
                for x in data:
                    records_to_insert.append((x['ItemID'], x['PurchaseStatus'], x['Factory'], x['ProductionYear'],
                                              x['Color'], x['PowerSupply'], productDict[(x['Category'], x['Model'])]))

                del records_to_insert[0]

                cursor = connection.cursor()
                cursor.executemany(mySql_insert_query, records_to_insert)
                connection.commit()
                messagebox.showinfo("Success", str(cursor.rowcount) + " Record inserted successfully into Item table", parent=self.root)
                print(cursor.rowcount, "record inserted successfully into Item table")

            except mysql.connector.Error as error:
                messagebox.showerror("Error", "Failed to insert record into MySQL table {}".format(error), parent=self.root)
                print("Failed to insert record into MySQL table {}".format(error))

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
                    print("MySQL connection is closed")

    def product_list(self):
        con=mysql.connector.connect(host=self.host.get(),
                                    database=self.database.get(),
                                    user=self.user.get(),
                                    password=self.password.get())
        cur=con.cursor()
        cur.execute("select category, productModel, productID from Product")
        rows=cur.fetchall()
        con.close()
        return rows


main = ItemImport(root)
root.mainloop()
