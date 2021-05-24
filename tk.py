#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

windowHeight = 600
windowWidth = 800
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
centerX = int((screenWidth - windowWidth)/2)
centerY = int((screenHeight - windowHeight)/2)
minWidth = 200
minHeight = 150
maxWidth = 1000
maxHeight = 750

root.title("Title of the window")
title = root.title()

root.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')
root.resizable(True, True)
root.minsize(minWidth, minHeight)
root.maxsize(maxWidth, maxHeight)

root.attributes('-alpha', 0.7)

tk.Label(root, text="This is a message").pack()
ttk.Label(root, text="themed Label").pack()
label3 = ttk.Label(root)
label3['text'] = 'label and dictonary'
label3.pack()
label4 = ttk.Label(root)
label4.config(text='label using config()')
label4.pack()
ttk.Button(root, text="this is a button").pack()
ttk.Checkbutton(root, text="checkbutton").pack()
ttk.Entry(root, text="Entry").pack()
ttk.Frame(root, height=30, width=50).pack()
ttk.Label(root, text="Label").pack()
ttk.LabelFrame(root, text="LabelFrame").pack()
ttk.Menubutton(root, text="PanedWindow").pack()
ttk.Radiobutton(root, text="RadioButton").pack()
ttk.Scale(root, from_=0, to=50, orient="horizontal").pack()
ttk.Scrollbar(root, orient="vertical").pack()
ttk.Spinbox(root, text="Spinbox").pack()

def display_text():
    global entry
    string = entry.get()
    somelabel.configure(text=string)

somelabel = ttk.Label(root, text="", font=("Courier 22 bold"))
somelabel.pack()
entry = ttk.Entry(root, width=50)
entry.focus_set()
entry.pack()
ttk.Button(root, text="Okay", width = 2, command = display_text).pack()

root.mainloop()
