from menu import coffee_menu, resources
from logo import coffee_cup
import sys
import os

profit = 0
machine_on = True

def print_coffee_menu():
  for coffee in coffee_menu:
    print(coffee)


def is_resource_sufficient(order_ingredients:dict)->bool:
  '''Return True if drink can be made , else returns False'''
  for item in order_ingredients:
    if order_ingredients[item] >= resources[item]:
      print(f"Sorry there is not enough {item}")
      return False
    
  return True


def process_money():
  '''Returns the total money by User'''
  total = int(input("\nPlease enter the money amount you payed? : $"))
  return total


def is_transaction_successful(money_received,drink_cost):
  '''Returns True if the transaction is successful , or False if the there is no sufficient money'''

  if(money_received >= drink_cost):
    change = round(money_received - drink_cost , 2)
    print('-----------------------------------------------')
    print(f"Here is ${change} in change")
    print('-----------------------------------------------')
    global profit
    profit += drink_cost
    return True
  else:
    print('-----------------------------------------------')
    print("Sorry that's not enough money. Money refunded.")
    print('-----------------------------------------------')
    return False


def make_cofee(drink_name , order_ingredients):
  '''deduct the required ingredients from the resources.'''
  for item in order_ingredients:
    resources[item] -= order_ingredients[item]
  print(f"Here is Your {drink_name}")
  print(coffee_cup)  
  

while machine_on:
  print("Welcome to py coffee machine.")
  print_coffee_menu()
  choice = input("\nWhat Would you like? : ")

  if(choice == "off"):
    machine_on = False
    
  elif(choice == "report"):
    print('--------------------------------------')
    print(f"Water  : {resources["water"]} ml")
    print(f"Milk   : {resources["milk"]} ml")
    print(f"Coffee : {resources["coffee"]} ml")
    print(f"Profit : ${profit}")
    print('--------------------------------------\n')

  elif(choice in coffee_menu):
      drink_data = coffee_menu[choice]
      if(is_resource_sufficient(drink_data["ingredients"])):
        payment = process_money()
        if(is_transaction_successful(payment , drink_data["cost"])):
          make_cofee(choice, drink_data["ingredients"])
      
      print("Press any key to continue...")
      sys.stdin.read(1)
      os.system("clear")
  
  else:
    print("Wrong Input")