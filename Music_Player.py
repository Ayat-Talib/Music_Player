import tkinter as Tk
import pygame
import os 
from tkinter import filedialog
pygame.mixer.init()

win = Tk.Tk()
win.geometry("400x350")  # for window size
win.configure(bg="Black")  # for background color
win.title("Music Player")

current_track = ""
paused = False

def load_music():
    global current_track
    current_track = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
    if current_track:
        track_label.config(text=os.path.basename(current_track))

def play_music():
    global paused
    if current_track:
        if not paused:
         pygame.mixer.music.load(current_track)
         pygame.mixer.music.play()
        else:
            pygame.mixer.music.unpause()
        paused = False

def Pause_music():
    global paused
    if current_track:
        pygame.mixer.music.pause()
        paused= True
def Stop_music():
    global paused
    if current_track:
        pygame.mixer.music.stop()
        paused = False

# Create the Buttons And Labels
Tk.Button(win, text= "LOAD", width= 30, bd=1,  font=3, bg ="lightgray", fg= "black", command=load_music).pack(pady= 7)
Tk.Button(win, text= "PLAY", width= 30, bd=1, font=3, bg ="blue", fg= "white", command= play_music).pack(pady= 7)
Tk.Button(win, text= "PAUSE",  width= 30,bd=1,  font=3, bg ="Green", fg= "white", command=Pause_music).pack(pady= 7)
Tk.Button(win, text= "STOP", width= 30,bd=1, font=3, bg ="red", fg= "white",  command=Stop_music).pack(pady= 7)
track_label = Tk.Label(win, text="No track loaded", bg = "black", fg= "white", )
track_label.pack(pady=5)

win.mainloop()