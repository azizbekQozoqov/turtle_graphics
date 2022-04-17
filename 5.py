import datetime
from time import strftime
from tkinter import *
from tkinter import font
from tkinter.ttk import *


win = Tk()
win.attributes("-topmost", True)
win.resizable(False, False)
win.title("Simple mini clock")

digital = font.Font(family="ds-digital", size=50)

l1 = Label(win, text="", font=digital)
l1.pack()


while True:
    now = datetime.datetime.utcnow()
    format = f"""{strftime("%H:%M:%S  %p")}"""
    l1.config(text=format, background="#000000", foreground="cyan")
    win.update()