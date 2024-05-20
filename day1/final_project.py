#Project Title : Band Name Generator

#Description : The Prompt will ask the user for their city name and pet name and then it will concatenate the two strings and gives it as an output which the user can use as their band name.


#---------------------------solution-----------------------------------
print('hi :) welcome to the band name generator project.\n')

city_name = input('Enter your city name : \n')
pet_name = input('Enter your pet name : \n')

band_name = city_name + ' ' + pet_name
print('Your band name could be : ',band_name)