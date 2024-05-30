'''
Problem : The below code is not printing anything.
          Try to find out the bug in below code
'''

for i in range(1,20):
  if i == 20:
    print("Reached the end.")

'''
solution : The range function takes a starting and ending numbers but , the ending number is not included.
So, the loop is running from 1 till 19 , and 20 is never coming.

To reach 20 , we need to increase the ending number by 1
'''


for i in range(1,21):
  if i == 20:
    print("Reached the end.")

'The above code correctly prints the output : '
# Reached the end.