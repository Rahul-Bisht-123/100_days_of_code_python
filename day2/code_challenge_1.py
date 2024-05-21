# Task : Take two digit number from the user as an input and then add the both digits.

# for ex : 45 => 4 + 5 => 9


# --------------------solution----------------------
number = input("Enter a two digit number : ")
first_number = number[0]
second_number = number[1]

# sum = first_number + second_number  (this will concatenate the two 'str' numbers, not add.)

sum  = int(first_number) + int(second_number)
print(sum)