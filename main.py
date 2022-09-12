import tkinter as tk
import fnmatch
import os
from PIL import Image, ImageTk
from pygame import mixer

canvas = tk.Tk()
canvas.title("music player")
canvas.geometry('600x800')
canvas.config(bg='white')

rootpath ="C:\\Users\dp992\PycharmProjects\music player\songa"
pattern = "*.mp3"

mixer.init()

pre = Image.open('prev.png')
pre= pre.resize((40,40))
nex = Image.open('next.png')
nex=nex.resize((40,40))
ply = Image.open('play.png')
ply=ply.resize((40,40))
pau = Image.open('pause.png')
pau=pau.resize((40,40))

prev_img = ImageTk.PhotoImage(pre)
next_img = ImageTk.PhotoImage(nex)
play_img = ImageTk.PhotoImage(ply)
pause_img = ImageTk.PhotoImage(pau)

def select():
    label.config(text=listbox.get("anchor"))
    mixer.music.load(rootpath+'\\'+listbox.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listbox.select_clear('active')

def play_next():
    next_song = listbox.curselection()
    next_song=next_song[0]+1
    next_song_name = listbox.get(next_song)
    label.config(text=next_song_name)
    mixer.music.load(rootpath+'\\'+next_song_name)
    mixer.music.play()

    listbox.select_clear(0,'end')
    listbox.activate(next_song)
    listbox.select_set(next_song)

def play_prev():
    prev_song = listbox.curselection()
    prev_song=prev_song[0]-1
    prev_song_name = listbox.get(prev_song)
    label.config(text=prev_song_name)
    mixer.music.load(rootpath+'\\'+prev_song_name)
    mixer.music.play()

    listbox.select_clear(0,'end')
    listbox.activate(prev_song)
    listbox.select_set(prev_song)

def pause_song():
    if stopbutton['text'] == "stop":
        mixer.music.pause()
        stopbutton['text'] = 'play'
    else:
        mixer.music.unpause()
        stopbutton['text'] ="stop"

listbox = tk.Listbox(canvas , fg="black", bg="light pink", width=100, font=('poppins',14))
listbox.pack(padx=30,pady=80)

label = tk.Label(canvas, text='', bg='white', fg='black', font=('times new roman ', 15))
label.pack(pady=15)

top = tk.Frame(canvas, bg='white')
top.pack(padx=10, pady=5, anchor='center')

prevbutton = tk.Button(canvas, text='prev', image=prev_img, bg='white', borderwidth=0, command=play_prev )
prevbutton.pack(pady=15,padx=15, in_=top, side='left')

playbutton = tk.Button(canvas, text='play', image=play_img, bg='white', borderwidth=0, command=select)
playbutton.pack(pady=15,padx=15, in_=top, side='left')

stopbutton = tk.Button(canvas , text='stop', image=pause_img, bg='white', borderwidth=0, command=stop )
stopbutton.pack(pady=15,padx=15, in_=top, side='left')

upbutton = tk.Button(canvas , text='up', image=next_img, bg='white', borderwidth=0, command=play_next )
upbutton.pack(pady=15,padx=15, in_=top, side='left')


for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listbox.insert('end', filename)
canvas.mainloop()