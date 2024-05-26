import os
print("Welcome to secret biding software \n")
biders_data = {}

def bid_winner(all_bidders_data:list):
  max_amount = 0
  winner_name = ""

  for current_name in all_bidders_data:
    current_amount = all_bidders_data[current_name]
    if(current_amount > max_amount):
      max_amount = current_amount
      winner_name = current_name

  print("\n--------------------------------------------------------")
  print(f"Winner name : {winner_name} || bid amount : ${max_amount}")
  print("--------------------------------------------------------\n")
  

while True:
  bider_name = input("Enter the person name : ")
  bider_amount  = float(input("Enter Your bid amount : $"))

  biders_data[bider_name] = bider_amount

  choice = input("\nIs there any other bidder . Types 'yes' or 'no' : ")

  if choice == "yes":
    os.system('clear')

  elif(choice == "no"):
    bid_winner(biders_data)
    break