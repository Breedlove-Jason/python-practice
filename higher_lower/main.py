# Import necessary modules and data
from art import logo, vs
from game_data import data
from random import randint, choice

# Print the game logo
print(logo)

# Initialize the score
score = 0

# Function to print the comparison data
def print_compare(choice_1, choice_2):
    # Print choice A details
    print(
        f"Compare A: {choice_1['name']}, a {choice_1['description']}, from {choice_1['country']}\n"
    )
    # Print the VS logo
    print(vs)
    # Print choice B details
    print(
        f"Against B: {choice_2['name']}, a {choice_2['description']}, from {choice_2['country']}\n"
    )

# Function to calculate the score
def calc_score(choice_1, choice_2, score):
    # Get user input
    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
    while True:
        # Check if choice A has more followers
        if int(choice_1["follower_count"]) > int(choice_2["follower_count"]):
            # Increase the score and print the current score
            score += 1
            print(f"You're right! Current score: {score}")
            return "a"
        else:
            # Print the final score and break the loop
            print(f"Sorry, that's wrong! Final score: {score}")
            break

# Function to check if the user wants to play again
def play_again(is_correct):
    # If the user was correct, return True
    if is_correct:
        return True

    # Ask the user if they want to play again
    play = input(f"\nDo you want to play again? Type 'y' or 'n': ").lower()
    print("\n")
    # Return True if the user wants to play again, False otherwise
    if play == "y":
        return True
    else:
        return False

# Start the game
play = True
# Get a random choice for choice A
choice_1 = choice(data)
while play:
    # Get a random choice for choice B
    choice_2 = choice(data)
    # Ensure choice A and choice B are not the same
    while choice_1 == choice_2:
        choice_2 = choice(data)
    # Print the comparison data
    print_compare(choice_1, choice_2)

    # Calculate the score
    is_correct = calc_score(choice_1, choice_2, score)
    if is_correct:
        # If the user was correct, increase the score and set choice A to the previous choice B
        score += 1
        choice_1 = choice_2
    else:
        # If the user was incorrect, reset the score and get a new random choice for choice A
        score = 0
        choice_1 = choice(data)

    # Check if the user wants to play again
    play = play_again(is_correct)