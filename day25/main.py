import csv 

with open(file="weather_data.csv") as weather_file:
  data = csv.reader(weather_file)
  temperatures = []
  for row in data:
    if row[1] != "temp":
      temperatures.append(int(row[1]))
  print(temperatures)