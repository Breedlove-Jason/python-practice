from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))
    # new_question = Question(question["text"], question["answer"])
    # question_bank.append(new_question)

# for _ in question_bank:
#     print(_.text)
#     print(_.answer)
quiz1 = QuizBrain(question_bank)
quiz1.next_question()
while quiz1.still_has_questions():
    quiz1.next_question()
    quiz1.check_answer()