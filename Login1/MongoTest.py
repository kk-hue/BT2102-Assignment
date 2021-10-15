from pymongo import MongoClient
from tkinter import *
import tkinter.messagebox as mb
from PIL import ImageTk, Image

#Making Connection
myclient = MongoClient("mongodb://localhost:27017/")

#database
db = myclient["OSHES"]

#Created or Swqitched to Collection
#name: product

Collection = db["product"]

light = Collection.find({"Category":"Lights"})
for lights in light:
    print(lights)
