'''
take user height and do check :
if height > 120 
if age < 12 , ticket = $5 
if age 12-18, ticket = $7
if age > 18 , ticket = $12 
'''

print("Welcome to wonderland \n")
height = int(input("Enter your height : "))

if height<120:
  print("NO ENTRY :( You are short. ")

else:
  print("You can ride")
  age = int(input("Enter your age : "))
  if age < 12:
    print("Ticket cost = $5")
  elif age <=18:
    print("Ticket cost = $7")
  else:
    print("Ticket cost = $12")