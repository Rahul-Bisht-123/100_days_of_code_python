# Project title : "Treasure hunt"

print("😇 : Welcome to the treasure island.Your mission is to find the treasure \n")

level_1 = input("🤠 : You are standing on the island gate on level1. choose 'left' or 'right' to move to next level2 : ")

if(level_1 == "left"):
  print("🤥 : Oops left door is full of water.You fallen water")
  print('''GAME OVER ❌''')

elif(level_1 == "right"):
  print("🤠 : Yeyy u chose right direction. You came to the level 2")
  print('''
              RED                 BLUE                 GREEN
            __________          __________           __________
           |  __  __  |        |  __  __  |         |  __  __  |  
           | |  ||  | |        | |  ||  | |         | |  ||  | |   
           | |__||__| |        | |__||__| |         | |__||__| |
           |  __  __()|        |  __  __()|         |  __  __()|
           | |  ||  | |        | |  ||  | |         | |  ||  | |
           | |  ||  | |        | |  ||  | |         | |  ||  | |
           |__________|        |__________|         |__________|
          
''')
  level_2 = input("🤠 : There are three gates in front of you. Choose 'red' , 'blue' or 'green' : ")

  if(level_2 == "red"):
    print("🤥 : Oops you entered in a room full of fire.")
    print('''GAME OVER ❌''')
    
  elif(level_2 == "blue"):
    print("🤥 : Oops you entered in a room full of water.")
    print('''GAME OVER ❌''')
    
  elif(level_2 == "green"):
    print("🥳 : Yeyy you found the treasure.\n")
    print('''🏆 WINNER 🏆''')

  else:
    print("🤥 : Wrong input. GAME OVER ❌")

else:
  print("🤥 : Wrong input. GAME OVER ❌")