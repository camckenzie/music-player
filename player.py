from tkinter import *
import pygame
from tkinter import filedialog


root = Tk()
root.title('Music Player')
root.iconbitmap('images/dj.ico')
root.geometry('500x300')

# Initialize Pygame Mixer
pygame.mixer.init()


# Add song function
def add_song():
    # What directory to look in initially,
    song = filedialog.askopenfilename(
        initialdir='music/', title='Choose A Song', filetypes=(('mp3 Files', '*.mp3'), ))
    # Strip out the directory info and .mp3 extension from song name
    song = song.replace(
        'C:/Users/Chris/Documents/GitHub/music-player/music/', '')
    song = song.replace('.mp3', '')
    # Add song to song box
    # where to insert, what to insert
    song_box.insert(END, song)

# Play selected song


def play():
    # Active = the one clicked
    song = song_box.get(ACTIVE)
    song = f'C:/Users/Chris/Documents/GitHub/music-player/music/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

# Stop playing current song


def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)


# Create Playlist Box
song_box = Listbox(root, bg='black', fg='green', width=60,
                   selectbackground='gray', selectforeground='black')
song_box.pack(pady=20)

# Define Player Control Buttons Images
prev_img = PhotoImage(file='images/previous.png')
next_img = PhotoImage(file='images/next.png')
play_img = PhotoImage(file='images/play.png')
pause_img = PhotoImage(file='images/pause.png')
stop_img = PhotoImage(file='images/stop.png')

# Create Player Control Frame
controls_frame = Frame(root)
controls_frame.pack()

# Create Player Control Buttons
prev_btn = Button(controls_frame, image=prev_img, borderwidth=0)
next_btn = Button(controls_frame, image=next_img, borderwidth=0)
play_btn = Button(controls_frame, image=play_img, borderwidth=0, command=play)
pause_btn = Button(controls_frame, image=pause_img, borderwidth=0)
stop_btn = Button(controls_frame, image=stop_img, borderwidth=0, command=stop)

prev_btn.grid(row=0, column=0, padx=10)
next_btn.grid(row=0, column=1, padx=10)
play_btn.grid(row=0, column=2, padx=10)
pause_btn.grid(row=0, column=3, padx=10)
stop_btn.grid(row=0, column=4, padx=10)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add 'Add Song' Menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label='Add Songs', menu=add_song_menu)
add_song_menu.add_command(label='Add One Song To PlayList', command=add_song)

root.mainloop()
