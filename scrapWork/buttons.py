from tkinter import *

root = Tk()


def myClick():
    myLabel = Label(root, text="Look! I clicked a button")
    myLabel.pack()


# Where we want it and what the text is for parameters
# For commands, don't use () or program will auto run it and not execute again
# fg = font color, bg = background color; can use hexcodes for colors too
myButton = Button(root, text="Click me",
                  command=myClick, fg='blue', bg='green')
myButton.pack()


root.mainloop()
