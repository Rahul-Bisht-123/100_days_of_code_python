from question_model import Question
from data import questions
from quiz_brain import QuizBrain

question_bank = []

for ques in questions:
  new_Question = Question(ques["text"] , ques["answer"])
  question_bank.append(new_Question)

quiz = QuizBrain(question_bank)

while(quiz.still_has_questions()):
  quiz.next_question()

print('-----------------------')
print("Quiz Finished")
print(f"Your ttal score is {quiz.score}/{quiz.question_number}")
print('-----------------------')
