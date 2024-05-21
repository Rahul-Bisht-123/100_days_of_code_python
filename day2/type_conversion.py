print(type('123'))  # <class 'str'>
print(type(123))    # <class 'int'>
print(type(123.77)) # <class 'float'>
print(type(True))   # <class 'bool'>


name_length = len(input('Enter Your Name '))

'''
print("Your name length is "+ name_length + "Characters")
TypeError: can only concatenate str (not "int") to str

'''

#type conversion from int to str
name_length_in_String = str(name_length)   

print("Your name length is " + name_length_in_String + " characters")