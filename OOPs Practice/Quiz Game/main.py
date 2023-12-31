from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = list()
for key in question_data:
    question_bank.append(Question(key["text"], key["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completer the quiz")
print(f"your final score was: {quiz.score}/{quiz.question_number}")


