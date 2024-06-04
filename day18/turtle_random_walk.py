from turtle import Turtle, Screen
import random


tim = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

directions = [0, 90, 180, 270]
tim.pensize(10)
tim.speed("fastest")

for _ in range (100): # set it 300 times to draw
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))#randomly to choose a random directions.


sc= Screen()
sc.exitonclick()