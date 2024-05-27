def format_name(first_name:str , last_name:str):
  '''This function will return the formatted name made by concatenating first_name and last_name'''
  formatted_first_name = first_name.title()
  formatted_last_name = last_name.title()
  return formatted_first_name + " " +formatted_last_name

print(format_name("john" , "cena"))  #John Cena

print(format_name.__doc__)
#This function will return the formatted name made by concatenating first_name and last_name