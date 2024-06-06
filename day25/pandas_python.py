import pandas

data = pandas.read_csv("weather_data.csv")
print(data)


#average of temperatures
avg = data["temp"].mean()
print(avg)

max_temp = data["temp"].max()
print(max_temp)

min_temp = data["temp"].min()
print(min_temp)