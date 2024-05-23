import random

'random.random() will generate a floating point number between 0 to 0.9'
random_float = random.random()
print(f"random_float =  {random_float}")

'random.ranint(1,10) will generate number from 1 to 10'
random_integer = random.randint(1,11)
print(f"random_integer = {random_integer}")


# heads and tails generator
heads_or_tails = random.randint(0,1)
if heads_or_tails == 1:
  print("coin shows : heads")
else:
  print("coin shows : tails")
