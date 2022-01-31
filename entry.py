from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()
# index number, default value
# This will put default text in inbox
e.insert(0, "Enter your name: ")


def myClick():
    hello = f'Hello {e.get()}'
    myLabel = Label(root, text=hello)
    myLabel.pack()


# Where we want it and what the text is for parameters
# For commands, don't use () or program will auto run it and not execute again
myButton = Button(root, text="Enter your name", command=myClick)

myButton.pack()


root.mainloop()
