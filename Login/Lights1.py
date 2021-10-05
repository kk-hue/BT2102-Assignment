from tkinter import *
# from tkinter.ttk import *
import tkinter.messagebox as mb
from PIL import ImageTk, Image

root=Tk()
class ProductView:

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
        #Show the label of the product
        self.title = Label(self.frame, text = "Product Catalogue", font=("Calibri", 20, 'bold'), bg="#FFD1C1")
        self.title.place(x=750, y=20)
        
        self.model = Label(self.frame, text = "Model", font=("Calibri", 15, 'bold'), bg="#FFD1C1")
        self.model.place(x=700, y=150)

        self.price = Label(self.frame, text = "Price", font=("Calibri", 15, 'bold'), bg="#FFD1C1")
        self.price.place(x=700, y=200)

        self.warranty = Label(self.frame, text = "Warranty", font=("Calibri", 15, 'bold'), bg="#FFD1C1")
        self.warranty.place(x=700, y=250)

        self.countStock = Label(self.frame, text = "Items in stock", font=("Calibri", 15, 'bold'), bg="#FFD1C1")
        self.countStock.place(x=700, y=300)

        self.Color = Label(self.frame, text = "Color", font=("Calibri", 15, 'bold'), bg="#FFD1C1")
        self.Color.place(x=700, y=350)

        self.Factory = Label(self.frame, text = "Factory", font=("Calibri", 15, 'bold'), bg="#FFD1C1")
        self.Factory.place(x=700, y=400)

        self.ProductYear = Label(self.frame, text = "Production Year", font=("Calibri", 15, 'bold'), bg="#FFD1C1")
        self.ProductYear .place(x=700, y=450)


        

        #Add photo for safe and lock

        #Photo or Label is clickable (make all same size) redirect to the page with description and add quantity to cart

        #Purchase button (When purchase, it will reflect the order change on profile page)
        #Pop up button if purchase is successful by customer
        purchase=Button(self.frame, text="Purchase", font=("Cambria", 15, "bold"), fg="black", bg="#FFD1C1", command=self.receipt)
        purchase.place(x=800, y=520)

        self.backBtn = Button(self.frame, text = "Back", activebackground = "#00B0F0",
                              activeforeground="white", fg="black",
                              bg="#FFD1C1", font=("Calibri", 15, 'bold'),
                              command=self.back_Lights)
        self.backBtn.place(x=950, y=520, width=100)

    def back_Lights(self):
        self.root.destroy()
        import LightsView


    def receipt(self):
        self.root.destroy()
        import Receipt
        

main = ProductView(root)
root.mainloop()
