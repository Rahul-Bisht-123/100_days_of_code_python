'''
this code will give generate a random password based on
the requirements given by the user
'''

import random
print("Welcome to the Password Generator \n")

password_length = int(input("What length password do you want : "))

lower_case_alphabets_length = int(input("How many lower case alphabets do you want in password : "))
upper_case_alphabets_length = int(input("How many upper case alphabets do you want in password : "))
digits_length = int(input("How many digits do you want in password : "))
symbols_length = int(input("How many symbols do you want in password : "))

Lowercase_Alphabets_List =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

Uppercase_Alphabets_List = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

Symbols_List = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

Digits_List = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# ----------------creating password with user requirements---------

small_letters = ''
capital_letters = ''
numbers = ''
symbols = ''

for i in range(1, lower_case_alphabets_length+1):
  small_letters += random.choice(Lowercase_Alphabets_List)

for i in range(1, upper_case_alphabets_length+1):
  capital_letters += random.choice(Uppercase_Alphabets_List)

for i in range(1, digits_length+1):
  numbers += random.choice(Digits_List)

for i in range(1, symbols_length+1):
  symbols += random.choice(Symbols_List)

password  = small_letters + symbols + capital_letters + numbers
print(password)