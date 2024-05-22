# Take user height(meter) and weight(kg) and calculate the bmi
'''
Under 18.5 : underweight
Over 18.5 below 25 : normal weight
25-30 : overweight
30-35 : obese
>35 : clincally obese
'''

print("Welcome to bmi calculator \n")

height = float(input("Enter Your height in metres : "))
weight = float(input("Enter Your weight in Kg : "))

bmi = round(weight / (height * height)  , 1)

if bmi < 18.5:
  print(f"Your bmi is {bmi} , you are under weight")
elif bmi < 25:
  print(f"Your bmi is {bmi} , you are normal weight")
elif bmi < 30:
  print(f"Your bmi is {bmi} , you are over weight")
elif bmi < 35:
  print(f"Your bmi is {bmi} , you are obese")
else:
  print(f"Your bmi is {bmi} , you are clinically obese")
