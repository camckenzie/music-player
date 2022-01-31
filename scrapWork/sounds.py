from tkinter import *
import pygame

root = Tk()
root.title('Music Player')
root.iconbitmap('images/dj.ico')
root.geometry('500x400')

# Need this to turn on pygame and sounds
pygame.mixer.init()


def play():
    # loads the song
    pygame.mixer.music.load('music/Slow.mp3')
    # plays it and determines how many times it will play
    pygame.mixer.music.play(loops=0)


def stop():
    pygame.mixer.music.stop()


my_button = Button(root, text='Play Song',
                   font=('Helvetica', 32), command=play)
my_button.pack(pady=20)

stop_button = Button(root, text='Stop', command=stop)
stop_button.pack(pady=20)

root.mainloop()
