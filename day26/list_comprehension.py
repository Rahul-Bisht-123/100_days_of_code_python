numbers  = [1,2,3,4,5]

new_list_of_sqaures = [num**2 for num in numbers]
new_list_of_cubes = [num**3 for num in numbers]

print(new_list_of_sqaures)   # [1, 4, 9, 16, 25]
print(new_list_of_cubes)     # [1, 8, 27, 64, 125]

#-------------------------------------------------------

name = "monkey"
letters = [letter for letter in name]
print(letters)   # ['m', 'o', 'n', 'k', 'e', 'y']

#-------------------------------------------------------

numbers_range = [num for num in range(1,5)]
numbers_range_times_two = [num*2 for num in range(1,5)]

print(numbers_range)            # [1, 2, 3, 4]
print(numbers_range_times_two)  # [2, 4, 6, 8]

#-------------------------------------------------------

names = ["jack" , "jake" , "paul" , "leo" , "tim" , "kim", "jane"]

names_of_len3 = [name for name in names if len(name)==3]
names_of_len4 = [name for name in names if len(name)==4]

names_of_len3_in_caps = [name.upper() for name in names if len(name)==3]
names_of_len4_in_caps = [name.upper() for name in names if len(name)==4]

print(names_of_len3)   # ['leo', 'tim', 'kim']
print(names_of_len4)   # ['jack', 'jake', 'paul', 'jane']

print(names_of_len3_in_caps)  # ['LEO', 'TIM', 'KIM']
print(names_of_len4_in_caps)  # ['JACK', 'JAKE', 'PAUL', 'JANE']


numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers  = [nums for nums in numbers if nums%2==0]
print(even_numbers)