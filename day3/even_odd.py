# Take a number from the User and check whether the number is even or odd

print("Welcome to odd even calculator")
number = int(input("Enter the number to check for odd and even : "))

if number%2 == 0:
  print(f"{number} is even")
else:
  print(f"{number} is odd")