marks = input("Enter the marks with space in between : ")

max_marks = 0
for mark in marks.split(" "):
  cur_mark = int(mark)
  if(max_marks < cur_mark):
    max_marks = cur_mark

print(max_marks)