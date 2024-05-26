travel_log = [
  {
    "country" : "Dubai",
    "visits" : 12,
    "cities" : ["c1" , "c2" , "c3"]
  },
  {
    "country" : "India",
    "visits" : 12,
    "cities" : ["i1" , "i2" , "i3"]
  }
]

# function to add new data in travel log
def add_new_travel_log(country_name:str , visits_count:int , cities_list:list):
  new_data = {
    "country" : country_name,
    "visits" : visits_count,
    "cities" : cities_list
  }
  travel_log.append(new_data)


print(travel_log)
add_new_travel_log("Russia" , 23 , ["r1" , "r2" , "r3"])
print(travel_log)