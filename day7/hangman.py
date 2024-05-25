from words_list import word_list

#step1 : randomly choose a word from the word_list

import random

random_word = random.choice(word_list)
print(f"word generated = {random_word} \n")


# step2 : create an list called display that contains the underscore equal to the len of the random_word

display = []
for i in range(len(random_word)):
  display.append("_")

print(display)

#step3 : Ask the user to guess a letter and store it in a variable called guess. Make the guess lowercase

chances = 6
while '_' in display:
  if(chances == 0):
    break

  guess = input("Guess a word : ").lower()
  print(f"You guessed letter = {guess} \n")

  found = False
  for i in range(len(random_word)):
    if guess == random_word[i]:
      found = True
      display[i] = guess

  if not found:
    chances -= 1
    print("Oops You guessed wrong 🤥")
  print(display , " || " ,  f"wrong guesses pending = {chances}")


print("----------------------------------")
if "_" not in display:
  print("You Win 🥳")

else:
  print("All chances over . You Lose 🙃")
print("----------------------------------")