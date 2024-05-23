heights = input("enter the heights with a space in between : ")

sum = 0
count=0
for height in heights.split(" "):
  count += 1
  sum += int(height)

average = round(sum/count , 2)
print(f"sum = {sum}")
print(f"count = {count}")
print(f"average = {average}")