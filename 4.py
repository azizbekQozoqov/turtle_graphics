"""JavaScript logo using turtle"""
from turtle import *

wn = Screen()
root = wn.cv._rootwindow
root.resizable(False, False)
root.geometry("600x600")

hideturtle()
up()
goto(-100, -300)

bgcolor("yellow")
write("JS", font=("Consolas", 240))


mainloop()