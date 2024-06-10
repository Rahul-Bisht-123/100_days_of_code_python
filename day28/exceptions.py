try: 
  numbers  = [0,1,2,3,4,5,6]
  print(numbers[9])
  phones = {"name1" : 9988 , "name2" : 32223}
  print(phones["name3"])

except IndexError as message:
  print(f"error : {message}")   
  #error : list index out of range

except KeyError as error_message:
  print(f"error : key {error_message} not found")
  # error : key 'name3' not found