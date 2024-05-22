# code the following requirements for the love calculator 
'''
take name1 and name2 as input

digit1 = count the number of "t" , "r" ,"u" ,"e" in  both name
digit2 = count the number of "l" , "o" , "v" , "e" in both name

score = concatenate digit1 + digit2

if score<10 or score>90 : your score is {score}. you are like coke and mentos

if score between 40-50 : your score is {score}. you are alright together.

for all remaining scores : your score is {score}

'''

# ------------------------CODE--------------------------------------------

print("Welcome to the love calculator :) \n")

name1 = input("Enter name 1 : ")
name2 = input("Enter name 2 : ")

combined_name1_name2 = name1+name2

combined_name1_name2_lower = combined_name1_name2.lower()
combined_name1_name2_count_of_t = combined_name1_name2.count("t")
combined_name1_name2_count_of_r = combined_name1_name2.count("r")
combined_name1_name2_count_of_u = combined_name1_name2.count("u")
combined_name1_name2_count_of_e = combined_name1_name2.count("e")

digit1 = combined_name1_name2_count_of_t + combined_name1_name2_count_of_r + combined_name1_name2_count_of_u + combined_name1_name2_count_of_e

combined_name1_name2_count_of_l = combined_name1_name2.count("l")
combined_name1_name2_count_of_o = combined_name1_name2.count("o")
combined_name1_name2_count_of_v = combined_name1_name2.count("v")

digit2 = combined_name1_name2_count_of_l + combined_name1_name2_count_of_o + combined_name1_name2_count_of_v + combined_name1_name2_count_of_e


score = int(str(digit1) + str(digit2))

print("---------------------------------------------------------")

print(f"total t = {combined_name1_name2_count_of_t}")
print(f"total r = {combined_name1_name2_count_of_r}")
print(f"total u = {combined_name1_name2_count_of_u}")
print(f"total e = {combined_name1_name2_count_of_e}")
print(f"total l = {combined_name1_name2_count_of_l}")
print(f"total o = {combined_name1_name2_count_of_o}")
print(f"total v = {combined_name1_name2_count_of_v}")
print(f"total e = {combined_name1_name2_count_of_e}")


print("---------------------------------------------------------")
if(score<10 or score>90):
  print(f"score is {score} , you both are like coke and mentos") 

elif(score>40 and score<50):
  print(f"score is {score}, you both will be alright")

else:
  print(f"score is {score}. No comments")