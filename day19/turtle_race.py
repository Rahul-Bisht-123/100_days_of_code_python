import turtle as t
import random

screen = t.Screen()
screen.setup(height=500 , width=800)
user_bet = screen.textinput(title="Make a bet" , prompt="Type one color turtle from (red,blue,green,black,orange,pink)?")
colors = ['red' ,'blue' , 'green' , 'black' , 'orange' , 'pink']

is_race_on = False
y_axis = -140
all_turtles = []

for i in range(len(colors)):
  new_turtle = t.Turtle(shape='turtle')
  new_turtle.penup()
  new_turtle.color(colors[i])
  new_turtle.goto(x=-380 , y= y_axis)
  y_axis += 57
  all_turtles.append(new_turtle)

if user_bet:
  is_race_on = True

while is_race_on:
  for one_turtle in all_turtles:
    if one_turtle.xcor() > 365:
      is_race_on = False
      winning_turtle = one_turtle.pencolor()
      if winning_turtle == user_bet:
        print(f"You win😎. The {winning_turtle} turtle is the winner")
      else:
        print(f"You lose🙃. The {winning_turtle} turtle is the winner")

    rand_distance = random.randint(0, 10)
    one_turtle.forward(rand_distance)




screen.exitonclick()