from turtle import *
import colorsys

speed(0)
pencolor("#ffc0cb")
pensize(2)
def fluer():
  for i in range(300):
    circle(190-i, 90)
    left(90)
    circle(190-i, 90)
    left(18)

fluer()

mainloop()
