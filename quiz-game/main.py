from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

# Check if question_data is empty
if not question_data:
    print("No questions found for the chosen difficulty level. Please try again with a different difficulty level.")
    exit()

# Create a list of Question objects from the question_data
question_bank = [Question(question["question"], question["correct_answer"]) for question in question_data]

# Initialize the QuizBrain with the question bank
quiz = QuizBrain(question_bank)

# Start the quiz
while quiz.still_has_questions():
    quiz.next_question()

# Display the final score
print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

