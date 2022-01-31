from tkinter import *
from PIL import ImageTk, Image
import sqlite3


root = Tk()
root.title("Images")
root.iconbitmap('images/dj.ico')
root.geometry('400x400')

# Databases

# Create a database/connect to one
conn = sqlite3.connect('address_book.db')

root.mainloop()
