students_marks = {
  "Aman" : 99,
  "Bob" : 65,
  "Cony" : 55,
  "Dany" : 88,
  "Erik" : 33
}

# This below function will convert the marks into grades

def marks_to_grades(mark):
  if(mark>=91 and mark<=100):
    return "Outstanding"
  elif(mark>=81 and mark<=90):
    return "Exceeds Expectations"
  elif(mark>=71 and mark<=80):
    return "Acceptable"
  elif(mark <= 70):
    return "Fail"

students_grades = {}
for key in students_marks:
   grades = marks_to_grades(students_marks[key])
   students_grades[key] = grades


print(students_marks)
print(students_grades)