import os

def add(num1 , num2):
  return num1 + num2

def sub(num1 , num2):
  return num1 - num2

def mul(num1 , num2):
  return num1 * num2

def divide(num1 , num2):
  return num1 / num2

operations = {
  "+" : add,
  "-" : sub,
  "*" : mul,
  "/" : divide,
}

def calculator():
  print("Welcme to the calculator Software. \n")

  off = False
  while not off:
    num1 = float(input("Enter the first number  : "))

    should_Continue = True
    while should_Continue:
      for op in operations:
        print(op)
      print()  

      sign = input("Enter the operation You want to use : ")
      if(sign not in operations):
        print("Wrong Operation Symbol")
        break
      
      num2 = float(input("Enter the next number  : "))

      calc_function = operations[sign]
      answer = calc_function(num1 , num2)
      print("------------------------------------------------")
      print(f"{num1} {sign} {num2} = {answer}")
      print("------------------------------------------------")
      print()

      switch = input(f'''Do You want to continue this calcultion with value {answer} , Type 'yes'.\nType 'no' for fresh calculator instance.\nType 'exit' to off the calculator :  ''')
      if(switch == "exit"):
        print("\nThank You for using it. Have a good day" + "👋🏻")
        off = True
        break 

      elif(switch == "yes"):
        num1 = answer

      elif(switch == "no"):
        os.system('clear')
        calculator()

      else:
        print("Wrong input")
        break

calculator()