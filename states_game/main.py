import turtle
import pandas as pd

# Load states data
STATES_DATA = "50_states.csv"
STATES = pd.read_csv(STATES_DATA)
STATES_LIST = STATES["state"].to_list()

# Screen setup
screen = turtle.Screen()
screen.title("U.S. States Game")
IMAGE = "blank_states_img.gif"
screen.addshape(IMAGE)
turtle.shape(IMAGE)


# Function to prompt user for a state guess
def pick_state(title, prompt):
    answer = screen.textinput(title=title, prompt=prompt)
    return answer.title() if answer else None


# Initialize score and correct guesses list
score = 0
correct_guesses = []

# Main game loop
while len(STATES_LIST) > 0:
    answer_state = pick_state(
        f"{score}/50 States Correct", "What's another state's name?"
    )

    # Handle closure of the text input dialog (cancel button)
    if not answer_state:
        print("Game exited by the user.")
        break

    # Check if the guessed state is correct and update game state
    if answer_state in STATES_LIST:
        # Retrieve the state data from the DataFrame
        state_data = STATES[STATES.state == answer_state].iloc[0]

        # Move the turtle to the state's coordinates and write the state name
        marker = turtle.Turtle()
        marker.hideturtle()
        marker.penup()
        marker.goto(state_data.x, state_data.y)
        marker.write(answer_state, align="center")

        # Update the lists and score
        correct_guesses.append(answer_state)
        STATES_LIST.remove(answer_state)
        score += 1
        print(f"{answer_state} - Yes")
    else:
        print(f"{answer_state} - Not a US state or already guessed")

# Hide the screen on game exit
turtle.mainloop()  # Keeps the window open even after the game loop ends
