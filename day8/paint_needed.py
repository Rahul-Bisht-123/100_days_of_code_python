length = float(input("Enter the length of the wall : "))
width = float(input("Enter the width of the wall : "))

import math

def calc_paint(Length , Width):
  area = length * width

# 1 paint can can fill 5m square
  cans_needed = math.ceil(area / 5)

  print(f"\nWall Area = {area}\n")
  print(f"Paint cans needed = {cans_needed}")


calc_paint(length , width)