def format_name(f_name:str , l_name:str):
  formatted_f_name = f_name.title()
  formatted_l_name = l_name.title()
  return formatted_f_name + " "+ formatted_l_name

print(format_name("john" , "kuMAR"))    # John Kumar
print(format_name("moHAN" , "siNGH"))   # Mohan Singh