from turtle import Turtle,Screen
import time
from snake import Snake

screen = Screen()
screen.bgcolor('black')
screen.setup(width=600 , height=600)
screen.title('SNAKE GAME 🐍')
screen.tracer(0)

snake = Snake()
screen.listen()

screen.onkey(fun= snake.up, key="Up")
screen.onkey(fun= snake.down, key="Down")
screen.onkey(fun= snake.left, key="Left")
screen.onkey(fun= snake.right, key="Right")


game_is_on = True
while game_is_on:
  screen.update()
  time.sleep(0.1)

  snake.move()


screen.exitonclick()