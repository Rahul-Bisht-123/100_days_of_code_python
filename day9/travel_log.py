# Nesting dictionary inside a dictionary
travel_log = {
  "France" : {
    "cities_visited" : ["City_F1", "City_F2", "City_F3"],
    "total_visits" : 12
  },
  "Germany" : {
    "cities_visited" : ["City_G1", "City_G2", "City_G3"],
    "total_visits" : 15
  },
}

print(travel_log)

# Nesting dictionary inside a list
travel_log2 = [
  {
    "Country_name": "U.S.A",
    "Cities_Visted": ["c1" , "c2" , "c3"],
    "Total expense" : 3_00_000
  },
  {
    "Country_name": "Dubai",
    "Cities_Visted": ["d1" , "d2" , "d3"],
    "Total expense" : 5_00_000
  },
  
]

print(travel_log2)