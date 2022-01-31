from tkinter import *

# This comes before any program
root = Tk()

# Creating a label widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is Chris")


myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)

# Create an event loop
# When you have a program running, it's always looping
root.mainloop()
