# Take a year as input from the user and then check whether it is a leap year or not.

print("Welcome to leap year software")

year = int(input("Enter a year : "))
if year%4 == 0:
  if year%100 == 0:
    if year%400 == 0:
      print(f"{year} is a leap year")
    else:
      print(f"{year} is not leap year")
  else:
    print(f"{year} is a leap year")
else:
  print(f"{year} is not a leap year")