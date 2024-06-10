fruits = ["apple" , "mango" , "orange"]

def make_pie(fruit_index):
  try:
    fruit = fruits[fruit_index]
  except IndexError:
    print("Fruit Pie")
  else:
    print(f"{fruit} pie")

make_pie(0)  # apple pie
make_pie(1)  # mango pie
make_pie(2)  # orange pie

make_pie(3)  # Fruit Pie
# IndexError: list index out of range