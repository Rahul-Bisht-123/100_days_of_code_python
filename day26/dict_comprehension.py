import random

students = ["Jake" , "John" ,"Jimmy", "Rose" , "Timy"]

# make a dictionary and assign marks to each student
students_score = {name:random.randint(1,100) for name in students}
print(students_score)


# make a dictionary of passed(>60) students 
passed_students = {std:students_score[std] for std in students_score if students_score[std] > 60}

print(passed_students)

#------------------------------------------------------------------------

'''count the word length in below sentence and make a dictionary'''

sentence = "what a rainy day in the ohio?"
sentence_count = {word:len(word) for word in sentence.split(" ")}
print(sentence_count)
# {'what': 4, 'a': 1, 'rainy': 5, 'day': 3, 'in': 2, 'the': 3, 'ohio?': 5}

#------------------------------------------------------------------------

'''convert the below temp in farenhites using dictionary comprehension'''

weathers = {
  "Mon" : 10,
  "Tue" : 10,
  "Wed" : 20,
  "Thr" : 20,
  "Fri" : 30,
  "Sat" : 30,
  "Sun" : 30
}

weather_f = {day:(temp * 9/5)+32 for (day, temp) in weathers.items()}
print(weather_f)
#------------------------------------------------------------------------