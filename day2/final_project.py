# Project Name : Tip Calculator
# Description : 
'''
- Take user input for total bill amount.
- Take user input for choosing tip percentage from 10 ,12 or 15
- Take user input for number for people splitting the bill.
- Return the amount per person have to pay.
'''


# ----------------------project code--------------------------------
print("Welcome to tip calculator")
print()
bill_amount = float(input("Enter the total bill : "))
tip_percent = float(input("Enter the tip percentage from 10, 12, 15 : "))
split_number = int(input("Enter the people count for split : "))

tip_amount = (tip_percent/100)*(bill_amount)

total_bill_with_tip = bill_amount + tip_amount

bill_split = round(total_bill_with_tip / split_number , 2)

print('-------------------------------------------------')
print(f"bill amount =  {bill_amount}")
print(f"tip amount =  {tip_amount}")
print(f"total bill after tip =  {total_bill_with_tip}")
print(f"bill for each person = {bill_split}")