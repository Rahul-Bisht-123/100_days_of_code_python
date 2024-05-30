import random
import os
from game_data import data
from logo import game_logo, vs

print(game_logo)

print("Welcome to the high and low game.\n")

def format_data(account):
  account_name = account["name"]
  account_country = account["country"]
  account_description = account["description"]

  return f"{account_name}, a {account_description}, from {account_country}."

def check_answer(user_guess , a_followers , b_followers):
  if a_followers > b_followers:
    return user_guess == "a"
  else:
    return user_guess == "b"

score = 0
game_on = True
account_b = random.choice(data)

while game_on:
  account_a = account_b
  account_b = random.choice(data)
  if(account_a == account_b):
    account_b = random.choice(data)

  print(f"Compare A : {format_data(account_a)}") 
  print(vs)
  print(f"Against B : {format_data(account_b)}") 

  user_guess = input("\nGuess who has more followers.Type 'A' or 'B' : ").lower()

  os.system("clear")
  print(game_logo)
  
  a_follower_count = account_a["followers_count"]
  b_follower_count = account_b["followers_count"]

  is_correct = check_answer(user_guess, a_follower_count, b_follower_count)

  if is_correct:
    score += 1
    print("\n---------------------------------------------------")
    print(f"Correct Answer 😎 || Current Score : {score}")
    print("---------------------------------------------------\n")

  else:
    game_on = False
    print("\n---------------------------------------------------")
    print(f"Wrong Answer 🤥 || Final Score : {score}")
    print("---------------------------------------------------\n")