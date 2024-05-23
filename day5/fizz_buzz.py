'''
print numbers from 1 to 100 
if num divisible by 3 print : fizz
if num divisible by 5 print : buzz
if num divisible by 3,5 print : fizz-buzz
'''

for num in range(1 , 101):
  if(num%3==0) and (num%5==0):
    print(f"{num} = fizz-buzz")
  elif(num%3 == 0):
    print(f"{num} = fizz")
  elif(num%5 == 0):
    print(f"{num} = buzz")
  else:
    print(num)
  
