import time
from tkinter import *
from xml.sax import SAXNotSupportedException
import pygame
from tkinter import filedialog
from mutagen.mp3 import MP3
import tkinter.ttk as ttk

root = Tk()
root.title('Music Player')
root.iconbitmap('images/dj.ico')
root.geometry('500x400')
# Initialize Pygame Mixer
pygame.mixer.init()


def runtime():
    '''Grab song length time info'''
    if stopped:
        # Stops slider time running at twice the speed
        return
    # Grab current song elapsed time
    current_time = pygame.mixer.music.get_pos() / 1000

    # throw up temp label to get data
    #slider_label.config(text=f'Slider: {int(my_slider.get())} and Song Pos: {int(current_time)}')
    # convert to time format
    converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))

    # Below 3 lines are from 'next' function
    # Get currently playing song
    #current_song = song_box.curselection()
    song = song_box.get(ACTIVE)
    song = f'C:/Users/Chris/Documents/GitHub/music-player/music/{song}.mp3'
    # Load song with Mutagen
    song_mut = MP3(song)
    # Get song length
    global song_length
    song_length = song_mut.info.length
    # convert to time format
    converted_song_length = time.strftime('%M:%S', time.gmtime(song_length))
    
    
    # Usually it is one second behind from Song Position, so we add a second
    current_time +=1
    
    if int(my_slider.get()) == int(song_length):
        status_bar.config(text=f'Time Elapsed: {converted_song_length} ')
    
    elif paused:
        pass
    
    elif int(my_slider.get()) == int(current_time):
        # slider has not been moved
        # Update the slider to position
        slider_postion = int(song_length)
        my_slider.config(to=slider_postion, value=int(current_time))
        
    else:
        # slider has been moved
        slider_postion = int(song_length)
        my_slider.config(to=slider_postion, value=int(my_slider.get()))
        
        # convert to time format
        converted_current_time = time.strftime('%M:%S', time.gmtime(my_slider.get()))
        
        # Output time to status bar
        status_bar.config(text=f'Time Elapsed: {converted_current_time} of {converted_song_length} ')  
        
        # Move this along by one second
        next_time = int(my_slider.get()) + 1
        my_slider.config(value=next_time)
        
    # Output time to status bar
    # status_bar.config(text=f'Time Elapsed: {converted_current_time} of {converted_song_length} ')   

    # Update slider position value to current song position
    # my_slider.config(value=int(current_time))
    


    # calls runtime function after every 1000ms (1 second)
    status_bar.after(1000, runtime)


def add_song():
    '''Add song function'''

    # What directory to look in initially,
    song = filedialog.askopenfilename(initialdir='music/', title='Choose A Song', filetypes=(('mp3 Files', '*.mp3'), ))
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
    # Set stopped variable to false so song can play
    global stopped
    stopped = False
    # Active = the one clicked
    song = song_box.get(ACTIVE)
    song = f'C:/Users/Chris/Documents/GitHub/music-player/music/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Call runtime function to get time
    runtime()

    # Update slider to position
    # slider_postion = int(song_length)
    # my_slider.config(to=slider_postion, value=0)
    # Get current volume
    #current_volume = pygame.mixer.music.get_volume()
    #slider_label.config(text=current_volume*100)
    
global stopped
stopped = False
def stop():
    '''Stops currently playing song'''
    # Reset Slider and Status bar
    status_bar.config(text='')
    my_slider.config(value=0)
    # Stop song from playing
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)

    # Clear the status bar
    status_bar.config(text='')
    
    # Set stop variable to true
    global stopped
    stopped = True


def next():
    '''Play the next song in the playlist'''
    # Reset Slider and Status bar
    status_bar.config(text='')
    my_slider.config(value=0)
    
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
    # Reset Slider and Status bar
    status_bar.config(text='')
    my_slider.config(value=0)
    
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
    stop()
    # Anchor is the highlighted song
    song_box.delete(ANCHOR)
    pygame.mixer.music.stop()


def delete_all():
    '''Delete all songs from playlist'''
    stop()
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


def slide(x):
    '''Slider function. Can drag to section of song or just view'''
    ##slider_label.config(text=f'{int(my_slider.get())} of {int(song_length)}')
    song = song_box.get(ACTIVE)
    song = f'C:/Users/Chris/Documents/GitHub/music-player/music/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0, start=int(my_slider.get()))


def volume(x):
    '''Create volume function'''
    pygame.mixer.music.set_volume(volume_slider.get())
    
    # Get current volume
    #current_volume = pygame.mixer.music.get_volume()
    #slider_label.config(text=current_volume*100)
    
# Create Main Frame
main_frame = Frame(root)
main_frame.pack(pady=20)

# Create Playlist Box
song_box = Listbox(main_frame, bg='black', fg='green', width=60, selectbackground='gray', selectforeground='black')
song_box.grid(row=0, column=0)

# Define Player Control Buttons Images
prev_img = PhotoImage(file='images/previous.png')
next_img = PhotoImage(file='images/next.png')
play_img = PhotoImage(file='images/play.png')
pause_img = PhotoImage(file='images/pause.png')
stop_img = PhotoImage(file='images/stop.png')

# Create Player Control Frame
controls_frame = Frame(main_frame)
controls_frame.grid(row=1, column=0, pady=20)

# Create volume label frame
volume_frame = LabelFrame(main_frame, text ='Volume')
volume_frame.grid(row=0, column=1, padx=20)

# Create Player Control Buttons
prev_btn = Button(controls_frame, image=prev_img, borderwidth=0, command=prev)
next_btn = Button(controls_frame, image=next_img, borderwidth=0, command=next)
play_btn = Button(controls_frame, image=play_img, borderwidth=0, command=play)
pause_btn = Button(controls_frame, image=pause_img,borderwidth=0, command=lambda: pause(paused))
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
add_song_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Add Songs', menu=add_song_menu)
add_song_menu.add_command(label='Add One Song To PlayList', command=add_song)

# Add multiple songs to playlist
add_song_menu.add_command(label='Add Multiple Songs To PlayList', command=add_multiple_songs)

# Create delete song menu
remove_song_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Remove Songs', menu=remove_song_menu)
remove_song_menu.add_command(label='Delete A Song From Playlist', command=delete)
remove_song_menu.add_command(label='Delete All Songs From Playlist', command=delete_all)

# Create status bar
# relief = outlline, border, anchor decides where text will be (right side)
status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
# fill=x means it will fill all of x axis, side determines it will be at bottom, ipady pushes text down a little
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

# Create Music Position Slider
my_slider = ttk.Scale(main_frame, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=360)
my_slider.grid(row=2, column=0, pady=10)

# Create Volume slider
# Volume scale is 0 to 1 for volume
volume_slider = ttk.Scale(volume_frame, from_=1, to=0, orient=VERTICAL, value=1, command=volume, length=125)
volume_slider.pack(pady=10)

# Create temporary slider label
#slider_label = Label(root, text='0')
#slider_label.pack(pady=10)

# Create status bar
# relief = outlline, border, anchor decides where text will be (right side)
status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
# fill=x means it will fill all of x axis, side determines it will be at bottom, ipady pushes text down a little
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

root.mainloop()
