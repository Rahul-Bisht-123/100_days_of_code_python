year_input = int(input("Enter the Year : "))
month_input = int(input("Enter the month : "))

months = {
    1: {"name": "January", "days": 31},
    2: {"name": "February", "days": 28},
    3: {"name": "March", "days": 31},
    4: {"name": "April", "days": 30},
    5: {"name": "May", "days": 31},
    6: {"name": "June", "days": 30},
    7: {"name": "July", "days": 31},
    8: {"name": "August", "days": 31},
    9: {"name": "September", "days": 30},
    10: {"name": "October", "days": 31},
    11: {"name": "November", "days": 30},
    12: {"name": "December", "days": 31}
}

def isLeap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        False
    else:
      return True
  else:
    return False

def days_in_month(year__:int , month__:int):
  if(month__ > 12):
    return "Invalid Month"
  
  leap_day = 0
  if(month__ == 2 and isLeap(year__)):
    leap_day = 1

  for month in months:
    if month == month__:
      month_data = months[month__]
      month_name = month_data["name"]
      month_days = month_data["days"]
      return f"{month_name} has {month_days + leap_day} days in Year {year__}"

print("\n-----------------------------------------")
print(days_in_month(year_input , month_input))
print("-----------------------------------------\n")