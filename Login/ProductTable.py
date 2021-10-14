from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

root = Tk()


class DisplayProduct:

    def __init__(self, root):

        self.root = root
        self.root.title("Product Display Table")
        self.root.geometry("1350x700+0+0")
        self.root.resizable(False, False)

        title = Label(self.root, text="Product Display Table", font=("calibri", 40, "bold"), bg="light blue", fg="white")
        title.pack(side=TOP, fill=X)

        # ======Manage Frame=======

        db_frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        db_frame.place(x=20, y=100, width=450, height=560)

        db_title = Label(db_frame, text="Product Display Table", bg="crimson", fg="white", font=("calibri", 25, "bold"))
        db_title.grid(row=0, columnspan=1, pady=20)


        # ======Detail Frame=======

        self.detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        self.detail_frame.place(x=500, y=100, width=800, height=560)

        lable_productResult = Label(self.detail_frame, text="Product Display Table", bg="crimson", fg="white", font=("calibri", 20, "bold"))
        lable_productResult.grid(row=0, column=0, pady=20, padx=7, sticky="w")

        # ====== Table Frame ========

        table_frame = Frame(self.detail_frame, bd=4, relief=RIDGE, bg="crimson")
        table_frame.place(x=10, y=70, width=760, height=480)


        self.product_table = ttk.Treeview(table_frame,
                                          columns=("productID", "Num of item sold", "Num of item unsold"))

        self.product_table.heading("productID", text="productID")
        self.product_table.heading("Num of item sold", text="Num of item sold")
        self.product_table.heading("Num of item unsold", text="Num of item unsold")

        self.product_table['show'] = 'headings'
        self.product_table.column("productID", width=100)
        self.product_table.column("Num of item sold", width=100)
        self.product_table.column("Num of item unsold", width=100)
        self.product_table.pack(fill=BOTH, expand=1)

        self.display_product()

    def display_product(self):
        try:
            productIDlist = self.productID_list()
            con = mysql.connector.connect(host="localhost", user="root", password="sxbl15302", database="oshes")
            result_list = []
            for productID in productIDlist:
                cur = con.cursor()
                cur.execute("SELECT * from Item WHERE productID = " + str(productID[0]))
                rows = cur.fetchall()
                inventory_count = 0
                sold_count = 0
                for row in rows:
                    if row[1] == 'Unsold':
                        inventory_count = inventory_count + 1
                    else:
                        sold_count = sold_count + 1

                result_list.append((productID, sold_count, inventory_count))
            for result in result_list:
                self.product_table.insert('',END,values=result)
            con.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)

    def productID_list(self):
        con = mysql.connector.connect(host="localhost", user="root", password="sxbl15302", database="oshes")
        cur = con.cursor()
        cur.execute("select productID from Product")
        rows = cur.fetchall()
        con.close()
        return rows

main = DisplayProduct(root)
root.mainloop()