from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["name" , "age" , "weight"]
table.add_row(["Person1" , 23 , "45Kg"])
table.add_row(["Person2" , 10 , "40Kg"])
table.add_row(["Person3" , 20 , "50Kg"])
table.add_row(["Person4" , 25 , "60Kg"])
table.add_row(["Person5" , 30 , "70Kg"])

print(table)