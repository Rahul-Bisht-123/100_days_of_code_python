# Task : Create a BMI calculator

# BMI = Weight(in kg) / Height(in metres) ** 2 

#-------------solution--------------

weight = int(input('Enter Your weight in Kg : '))
height = float(input('Enter Your height in meters : '))

bmi = (weight) / (height **2)
print("bmi = ",bmi)

bmi = (weight) // (height ** 2)
print("bmi = " ,bmi)