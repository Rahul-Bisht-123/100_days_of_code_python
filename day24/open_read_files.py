with open(file="a.txt") as file1:
  contents=file1.read()
  print(contents)

with open(file="b.txt" , mode='a') as file2:
  file2.write("hello file2 from python")
