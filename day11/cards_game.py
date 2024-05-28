# Give user a random card

import random

def deal_card():
  '''Returns a random card from the deck'''
  cards = [11, 2 ,3 , 4 , 5 , 6 , 7 , 8, 9 , 10 , 10 , 10 , 10]
  card = random.choice(cards)
  return card

def calculate_score(cards:list):
  '''returns the sum of the cards passed as arguments'''
  if sum(cards)==21 and len(cards) == 2:
    return 0
  
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)

def compare(user_score , computer_score):
  if user_score == computer_score:
    return "Draw 🤝"
  elif computer_score == 0:
    return "You Lose , opponent has black Jack 🥲"
  elif user_score == 0:
    return "You Win with black Jack 😎"
  elif user_score > 21:
    return "You Lose , Your score went over 21 🥲"
  elif computer_score > 21:
    return "You Win , opponent score went over 21 🥳"
  elif user_score > computer_score:
    return "You Win , your score is more than opponent 🥳"
  else:
    return "You Lose 🥲"
  
def play_game():

  print("\nWelcome to the Card Game \n")
  user_cards = []
  computer_cards = []

  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  isGameOver = False

  while not isGameOver:
    user_score  = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards : {user_cards} , current score : {user_score}")
    print(f"Computer's first card : {computer_cards[0]} ")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        isGameOver = True
      
    else:
      user_should_deal = input("\nType 'y' to get another cards or 'no' to pass : ")
      if(user_should_deal == "y"):
        user_cards.append(deal_card())

      else:
        isGameOver = True
      
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)


  print(f"\nYour final cards = {user_cards} , final score : {user_score}\n")
  print(f"\nComputer's final cards = {computer_cards} , final score : {computer_score}\n")
  print(compare(user_score , computer_score))

import os
while input("Do you want to play card game. Type 'yes' or 'no' : ") == "yes":
  os.system("clear")
  play_game()