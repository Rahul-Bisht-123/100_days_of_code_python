def format_name(f_name:str , l_name:str):

  if(f_name == "" or l_name == ""):
    return "Invalid Inputs"
  formatted_f_name = f_name.title()
  formatted_l_name = l_name.title()
  return formatted_f_name + " "+ formatted_l_name

print(format_name("john" , "kuMAR"))    # John Kumar
print(format_name("moHAN" , "siNGH"))   # Mohan Singh

print(format_name("" ,"king"))  #Invalid Inputs