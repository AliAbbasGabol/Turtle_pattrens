import turtle
import time
time.sleep(4)
t1 = turtle.Turtle()
# Create window to Display Pattern
screen = turtle.Screen()
# Set screen size
screen.setup(800,600)
#speed determines pen speed slow it down to see pattren in detail
t1.speed(40)
t1.pensize(2)
t1.penup()
t1.goto(200,0)
t1.pendown()

#a star moving a little bit then making another star
for i in range(16):
  for i in range(24):

    t1.left(226)
    t1.forward(144)
  t1.forward(40)