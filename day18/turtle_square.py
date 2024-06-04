from turtle import Turtle, Screen

myturtle = Turtle()
myturtle.color('blue')

def make_square():
  myturtle.forward(100)
  myturtle.left(90)
  myturtle.forward(100)
  myturtle.left(90)
  myturtle.forward(100)
  myturtle.left(90)
  myturtle.forward(100)

# make_square()

def make_dashed_line():
  for _ in range(10):
    myturtle.forward(10)
    myturtle.penup()
    myturtle.forward(10)
    myturtle.pendown()

make_dashed_line()

myscreen = Screen()
myscreen.exitonclick()