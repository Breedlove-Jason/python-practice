import requests
import html

# Get the difficulty level from the user's input
difficulty = input("Choose your difficulty level (easy, medium, hard): ").lower()

# API parameters for fetching questions
parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18,  # Science: Computers
    "difficulty": difficulty
}

# Fetch questions from the Open Trivia Database API
api_url = "https://opentdb.com/api.php"
response = requests.get(api_url, params=parameters)
response.raise_for_status()
data = response.json()

# Process and clean the question data
question_data = data["results"]
for question in question_data:
    question["question"] = html.unescape(question["question"])
    question["correct_answer"] = html.unescape(question["correct_answer"])
