from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Images")
root.iconbitmap('images/dj.ico')


my_img = ImageTk.PhotoImage(Image.open('images/play.png'))
myLabel = Label(image=my_img)
myLabel.pack()


root.mainloop()
