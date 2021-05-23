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

root.mainloop()
