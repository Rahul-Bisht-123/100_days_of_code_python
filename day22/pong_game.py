from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800 , height=600)
screen.title("Pong Game")
screen.tracer(0)

left_paddle = Paddle((-350 , 0))
right_paddle = Paddle((350, 0))
ball = Ball((0,0))
scoreboard = Scoreboard()


screen.listen()
screen.onkey(right_paddle.go_up , "Up")
screen.onkey(right_paddle.go_down, "Down")

screen.onkey(left_paddle.go_up , "w")
screen.onkey(left_paddle.go_down , "s")


game_is_on = True

while game_is_on:
  time.sleep(ball.move_speed)
  screen.update()
  ball.move()

  #detect wall collision
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()

  #detect ball collision with paddle
  if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
    ball.bounce_x()

  #detect right paddle misses the ball
  if ball.xcor() > 380:
    ball.reset_position()
    scoreboard.left_point()

  #detect left paddle misses the ball
  if ball.xcor() < -380:
    ball.reset_position()
    scoreboard.right_point()



screen.exitonclick()