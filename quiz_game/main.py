from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
# question = Question()
question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))
print(question_bank[-1].text)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")