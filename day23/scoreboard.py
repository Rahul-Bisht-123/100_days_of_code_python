from turtle import Turtle

FONT = ("Courier" , 24 , "normal")
ALIGN = "left"

class Scoreboard(Turtle):
  def __init__(self) -> None:
    super().__init__()
    self.level = 1
    self.hideturtle()
    self.penup()
    self.goto(-280 , 250)

  def update_scoreboard(self):
    self.clear()  
    self.write(f"Level: {self.level}" , align= ALIGN , font= FONT)

  def increase_level(self):
    self.level += 1
    self.update_scoreboard()

  def game_over(self):
    self.goto(-70,0)
    self.write("GAME OVER" , align= ALIGN , font= FONT)