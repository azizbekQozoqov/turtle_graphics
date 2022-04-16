from turtle import *

colors = ["red", "yellow", "green", "purple", "blue", "orange"]

p = Pen()
bgcolor("black")
speed(0)
for i in range(200):
  p.pencolor(colors[i%6])
  p.width(i/100+1)
  p.forward(i)
  p.left(59)
mainloop()
