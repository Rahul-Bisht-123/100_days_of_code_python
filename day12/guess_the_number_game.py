import os
import random

play_game = True

while play_game:
  print("Welcome to the guess the number Game.\n")
  guessing_chances = 0

  wrong_level_input = True
  while wrong_level_input:
    level = input("Type 'easy' or 'hard' to choose your level or Type 'exit' to exit the game : ")

    if(level == "easy"):
      guessing_chances = 10
      wrong_level_input = False

    elif(level == "hard"):
      guessing_chances = 5
      wrong_level_input = False

    elif(level == "exit"):
      wrong_level_input = False
      play_game = False
      print("\nGame Exited ..")
      break

    else:
      wrong_level_input = True
      print("Wrong input\n")
    
  if play_game == False:
    break

  print(f"\nComputer choosed a random number between 1 to 100. Try to guess it. 😄 || Guesses Pending : {guessing_chances} \n")
  computer_choosen_number = random.randint(1,100)
  print(f"Choosen Number : {computer_choosen_number} || Guesses Pending : {guessing_chances}")

  while(guessing_chances > 0):
    user_number = int(input("\nEnter the number you Guessed : "))

    if(user_number > computer_choosen_number):
      guessing_chances -= 1
      print(f"\nYou guessed too high. Try Low ⬇️ || Guesses Pending : {guessing_chances}")

    elif(user_number < computer_choosen_number):
      guessing_chances -= 1
      print(f"\nYou guessed too low. Try High ⬆️  || Gueeses Pending : {guessing_chances}")

    elif(user_number == computer_choosen_number):
      print("----------------------------")
      print("Correct Guess. You WIN 🥳 ")
      print("----------------------------\n")

      choice =  input("Do you want to play again . Type 'yes' or 'no' : ")
      if(choice == "no"):
       play_game = False
       print("Game exited...")
      
      elif(choice == "yes"):
        os.system("clear")
      
      else:
        print("Wrong Input")
        play_game = False
        break

      break

    else:
      print("Wrong input")  