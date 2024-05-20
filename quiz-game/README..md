 # Quiz Game

## Description

The Quiz Game project is a simple trivia game that fetches questions from the Open Trivia Database API based on the user's chosen difficulty level. The game presents each question to the user and checks their answers, keeping track of the score throughout the game.

## How to Use

1. Run the `main.py` script.
2. The game will prompt you to choose a difficulty level (easy, medium, hard).
3. The game will fetch 10 questions from the Open Trivia Database API.
4. Answer each question with "True" or "False".
5. The game will keep track of your score and display the final score at the end.

## Files

- `main.py`: The main script that runs the game.
- `quiz_brain.py`: Contains the `QuizBrain` class that handles the quiz logic.
- `question_model.py`: Contains the `Question` class that represents a quiz question.
- `data.py`: Fetches and processes the question data from the API.

## Running the Project

To run the project, navigate to the `quiz-game` directory and execute the `main.py` script using Python:

```bash
cd quiz-game
python main.py
```

```bash
quiz-game/
├── main.py
├── quiz_brain.py
├── question_model.py
├── data.py
└── README.md
```

Choose your difficulty level (easy, medium, hard): medium
Q.1: The HTML5 standard was published in 2014. (True/False): true
You got it right!
The correct answer was: True
Your current score is: 1/1

Q.2: The first computer virus was created in 1983. (True/False): false
That's wrong.
The correct answer was: True
Your current score is: 1/2

...
You've completed the quiz!
Your final score was: 7/10
