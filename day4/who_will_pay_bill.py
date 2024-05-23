import random

# this code will take names seperated by comma , then code will pick up a random person name and return it


names_string = input("Enter the people names sepereated by comma : ")

names_list = names_string.split(",")

random_integer = random.randint(0 , len(names_list)-1)
message_template = f"{names_list[random_integer]} will pay the bill"
print(random_integer)
print(message_template)