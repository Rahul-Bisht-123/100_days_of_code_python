# Code the follwing requirements for the theme park

'''
height:
<120 cm not allowed
>120 cm allowed , ask for there age

age:
<12    child ticket = $5
12-18  teen ticket = $7
<18 ,  adult ticket = $12

want_Pics:
True  : +$3
False : +$0

'''

print("Welcome to the theme park :) \n")

height = float(input("Enter your height in cm : "))
bill = 0

if(height<120):
  print("Not allowed :(")

else:
  print("Allowed :)")
  age = int(input("Enter your age : "))

  if(age < 12):
    print("Child ticket = $5")
    bill = 5
  elif(age < 18):
    print("Teen ticket = $7")
    bill = 7
  else:
    print("Adult ticket = $12")
    bill = 12

  print(f"bill = ${bill}")

  #check for pics
  want_pics = input("Do you want photos for extra $3? Type Y or N : ")
  if(want_pics == "Y"):
    bill += 3
  
  print(f"Want Photoes = {want_pics}")
  print(f"total bill = ${bill}")
