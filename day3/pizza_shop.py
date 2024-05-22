# code the following requirements for a pizza shop
'''
# take user input for size of pizza : small, medium, large
small pizza : $15
medium pizza : $20
large pizza : $25

# take input for the pepperoni : yes , no
pepperoni for small pizza : +$2
pepperoni for medium & large pizza : +$3

# take input for extra cheese : yes , no
extra chesse for any size pizza : +$1

'''


# --------------------CODE--------------------------

print("Welcome to RB pizza shop \n")

print("Small pizza  : $15")
print("Medium pizza : $20")
print("Large pizza  : $25\n")

bill = 0
pizza_cost = 0
pepperoni_cost = 0
extra_cheese_cost = 0

pizza_size = input("Please select your pizza size? Type small, medium or large : ")

# print()
print(f"\npizza selected = {pizza_size}")

if(pizza_size == "small"):
  bill += 15
elif(pizza_size == "medium"):
  bill += 20
elif(pizza_size == "large"):
  bill += 25
else:
  print("wrong input")

pizza_cost = bill

needs_pepperoni = input("\nDo you want pepperoni ? Type yes, no : ")
if (needs_pepperoni == "yes"):
  if(pizza_size=="small"):
    pepperoni_cost = 2
    bill += pepperoni_cost
  else:
    pepperoni_cost = 3
    bill += pepperoni_cost


needs_extra_cheese = input("Do you need extra cheese ? Type yes or no : ")
if(needs_extra_cheese == "yes"):
  extra_cheese_cost = 1
  bill += extra_cheese_cost

print("---------------------------------------------------------------")
print(f"pizza size = {pizza_size}, | cost = {pizza_cost}")
print(f"pepperoni added = {needs_pepperoni} , | cost = {pepperoni_cost}")
print(f"extra cheese added = {needs_extra_cheese}, | cost = {extra_cheese_cost}")
print("---------------------------------------------------------------")
print(f"total bill = ${bill}")