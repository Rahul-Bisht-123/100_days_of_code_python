'''
- Take user input for as a rock, paper or scissors
- generate a random choice from code as well
- compare both of them and return the winner
'''

import random

print('Welcome to the "rock" , "paper" , "scissors" game...\n')

user_choosed = input('''choose one from "rock" , "paper" , "scissors" ? : ''')

game_choices = ["rock" , "paper" , "scissors"]
code_choosed = random.choice(game_choices)


print(f"\nYou choosed : {user_choosed}")
print(f"The code choosed : {code_choosed}\n")


if(user_choosed == "rock"):
  if(code_choosed == "rock"):
    print("rock vs rock : draw")
  elif(code_choosed == "paper"):
    print("rock vs paper : You lose")
  elif(code_choosed == "scissors"):
    print("rock vs scissors : You win")

elif(user_choosed == "paper"):
  if(code_choosed == "rock"):
    print("paper vs rock : You win")
  elif(code_choosed == "paper"):
    print("paper vs paper : draw")
  elif(code_choosed == "scissors"):
    print("paper vs scissors : You lose")

elif(user_choosed == "scissors"):
  if(code_choosed == "rock"):
    print("scissors vs rock : You lose")
  elif(code_choosed == "paper"):
    print("scissors vs paper : You Win")
  elif(code_choosed == "scissors"):
    print("scissors vs scissors : draw")

else:
  print("wrong input by user")