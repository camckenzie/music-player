from tkinter import *
import pygame

root = Tk()
root.title('Music Player')
root.iconbitmap('images/dj.ico')
root.geometry('500x300')

# Initialize Pygame Mixer
pygame.mixer.init()

# Create Playlist Box

song_box = Listbox(root, bg='black', fg='green', width=60)
song_box.pack(pady=20)

root.mainloop()
