# These are some simple pattrens generated using turtle 
import turtle
screen = turtle.Screen()
import time

#for making any shape consider there outside angles as the moving pen moves with outside angles 
time.sleep(5)

# Create window to Display Pattern
t = turtle.Turtle()
s = turtle.Screen()
t.hideturtle()
# Setting Background color
s.bgcolor("white")
s.setup(1080,530)


# Speed of turle drawing
t.speed(60)
#t.pensize(1.3)

# this block makes a square at each end of triangle side 
t.hideturtle()
for i in range(80):
# this makes a triangle 
  for i in range(3):
# this makes a square
    for i in range(4):
      t.left(90)
      t.forward(60)
# outside angle of equilateral triangle are 120
    t.left(120)
    t.forward(200)
    
  t.left(125)
  t.forward(50)
time.sleep(2)
t.clear()



t.hideturtle()
for i in range(80):
  for i in range(3):
    
    t.left(120)
    t.forward(200)
    
  t.left(95)
  t.forward(100)

time.sleep(2)
t.clear()


t.hideturtle()
for i in range(200):
  for i in range(5):
  
    t.left(72)
    t.forward(160)

  t.left(73)
  t.forward(80)

time.sleep(2)
t.clear()  



t.hideturtle()
for i in range(160):
  for i in range(6):
  
    t.left(60)
    t.forward(120)
    turtle.update()
  t.left(73)
  t.forward(60)

time.sleep(2)
t.clear()  



t.hideturtle()
for i in range(250):
  for i in range(7):
  
    t.left(51.5)
    t.forward(100)
  t.left(73)
  t.forward(50)

time.sleep(2)
t.clear()



t.hideturtle()
for i in range(200):
  for i in range(8):
  
    t.left(45)
    t.forward(80)
  t.left(73)
  t.forward(50)

time.sleep(2)
t.clear()




t.hideturtle()
for i in range(200):
  for i in range(12):
  
    t.left(30)
    t.forward(50)
  t.left(73)
  t.forward(62.5)
  
time.sleep(2)
  