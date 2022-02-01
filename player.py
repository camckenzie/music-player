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
    '''Add song function'''

    # What directory to look in initially,
    song = filedialog.askopenfilename(
        initialdir='music/', title='Choose A Song', filetypes=(('mp3 Files', '*.mp3'), ))
    # Strip out the directory info and .mp3 extension from song name
    song = song.split('/')[-1]
    song = song.replace('.mp3', '')
    # Add song to song box
    # where to insert, what to insert
    song_box.insert(END, song)


def add_multiple_songs():
    '''Add multiple songs function'''

    songs = filedialog.askopenfilenames(
        initialdir='music/', title='Choose A Song', filetypes=(('mp3 Files', '*.mp3'), ))

    # Loop through song list and replace diretory info and mp3
    for song in songs:
        song = song.split('/')[-1]
        song = song.replace('.mp3', '')
        # Insert into playlist
        song_box.insert(END, song)


def play():
    '''Plays the selected song'''

    # Active = the one clicked
    song = song_box.get(ACTIVE)
    song = f'C:/Users/Chris/Documents/GitHub/music-player/music/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)


def stop():
    '''Stops currently playing song'''

    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)


def next():
    '''Play the next song in the playlist'''
    # Gives us current song playing in playlist in form of tuple (0,)
    next_song = song_box.curselection()
    # Add one to current song number
    next_song = next_song[0]+1
    # Grab song title from playlist
    song = song_box.get(next_song)

    # This is the entire play song function
    song = f'C:/Users/Chris/Documents/GitHub/music-player/music/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Move active bar in playlist box
    song_box.selection_clear(0, END)

    # Activate new song bar
    song_box.activate(next_song)

    # Set Active bar to Next Song
    song_box.selection_set(next_song, last=None)


def prev():
    '''Play the previous song in the playlist'''
    next_song = song_box.curselection()
    next_song = next_song[0]-1
    song = song_box.get(next_song)

    # This is the entire play song function
    song = f'C:/Users/Chris/Documents/GitHub/music-player/music/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    song_box.selection_clear(0, END)
    song_box.activate(next_song)
    song_box.selection_set(next_song, last=None)


def delete():
    '''Delete a song'''

    # Anchor is the highlighted song
    song_box.delete(ANCHOR)
    pygame.mixer.music.stop()


def delete_all():
    '''Delete all songs from playlist'''

    song_box.delete(0, END)
    pygame.mixer.music.stop()


# When we click pause, we need to know whether or not song has been paused or not
# Need to pass in this ability to know
# Create global pause variable
global paused
paused = False


def pause(is_paused):
    '''Pause and Unpause the current song'''
    # Want this global variable inside and outside function
    # So it they global variable is consistent inside and out the function
    global paused
    paused = is_paused

    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True


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
prev_btn = Button(controls_frame, image=prev_img, borderwidth=0, command=prev)
next_btn = Button(controls_frame, image=next_img, borderwidth=0, command=next)
play_btn = Button(controls_frame, image=play_img, borderwidth=0, command=play)
pause_btn = Button(controls_frame, image=pause_img,
                   borderwidth=0, command=lambda: pause(paused))
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

# Add multiple songs to playlist
add_song_menu.add_command(
    label='Add Multiple Songs To PlayList', command=add_multiple_songs)

# Create delete song menu
remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label='Remove Songs', menu=remove_song_menu)
remove_song_menu.add_command(
    label='Delete A Song From Playlist', command=delete)
remove_song_menu.add_command(
    label='Delete All Songs From Playlist', command=delete_all)

root.mainloop()
