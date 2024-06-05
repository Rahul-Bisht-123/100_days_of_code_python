from turtle import Turtle

class Paddle(Turtle):
  def __init__(self, position) -> None:
    super().__init__()

    self.color("white")
    self.shape("square")
    self.color("white")
    self.shapesize(stretch_len=1 , stretch_wid=5)
    self.penup()
    self.goto(position)

  def go_up(self):
    new_y = self.ycor() + 50
    self.goto(self.xcor() , new_y)

  def go_down(self):
    new_y = self.ycor() - 50
    self.goto(self.xcor() , new_y)
  