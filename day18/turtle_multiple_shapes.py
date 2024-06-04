from turtle import Turtle, Screen
import random

tim = Turtle()

sides_count = 3
while sides_count < 10 :
  tim.color(random.choice(['red','blue','green','orange','grey']))  
  for _ in range(sides_count):
    angle = 360 / sides_count
    tim.forward(100)
    tim.right(angle)
  sides_count += 1 


sh = Screen()
sh.exitonclick()