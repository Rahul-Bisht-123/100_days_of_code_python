# Task : Take user age and return the number of years , months and days left for him till he turns 90 years old.
# 

#-------------solution--------------

age = int(input('Enter Your age : '))

years_pending = 90 - age
months_pending = years_pending * 12
weeks_pending = months_pending * 4
days_pending = weeks_pending * 7

result = f"Your cuurent age is {age} , You have {years_pending} years , {months_pending} months , {weeks_pending} weeks , {days_pending} days pending till your 90 age."

print(result)