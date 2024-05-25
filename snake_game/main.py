from turtle import Turtle, Screen
from random import randint

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SNAKE_SIZE = 20
SNAKE_COLOR = "white"
FOOD_COLOR = "red"
GAME_SPEED = 100

# Global variables
snake_body = []
food = None
score = 0
score_display = Turtle()
score_display.hideturtle()
score_display.penup()
score_display.color("white")
score_display.goto(0, 260)


def create_turtle(x, y):
    """
    Creates a new turtle segment at the given x, y position.

    Args:
        x (int): The x-coordinate of the turtle segment.
        y (int): The y-coordinate of the turtle segment.

    Returns:
        Turtle: The newly created turtle segment.
    """
    new_turtle = Turtle()
    new_turtle.shape("square")
    new_turtle.color(SNAKE_COLOR)
    new_turtle.penup()
    new_turtle.goto(x, y)
    return new_turtle


def create_food():
    """
    Creates a new food turtle at a random position.

    Returns:
        Turtle: The newly created food turtle.
    """
    global food
    if food:
        food.goto(randint(-280, 280), randint(-280, 280))
    else:
        food = Turtle()
        food.shape("circle")
        food.color(FOOD_COLOR)
        food.penup()
        food.goto(randint(-280, 280), randint(-280, 280))
    return food


def move_up():
    if snake_body[0].heading() != 270:  # Prevents the snake from moving in the opposite direction instantly
        snake_body[0].setheading(90)  # 90 denotes up


def move_down():
    if snake_body[0].heading() != 90:  # Prevents the snake from moving in the opposite direction instantly
        snake_body[0].setheading(270)  # 270 denotes down


def move_left():
    if snake_body[0].heading() != 0:  # Prevents the snake from moving in the opposite direction instantly
        snake_body[0].setheading(180)  # 180 denotes left


def move_right():
    if snake_body[0].heading() != 180:  # Prevents the snake from moving in the opposite direction instantly
        snake_body[0].setheading(0)  # 0 denotes right


def move_snake():
    """
    Moves the snake forward by updating the position of each segment.
    """
    # Move the segments from tail to head
    for i in range(len(snake_body) - 1, 0, -1):
        x = snake_body[i - 1].xcor()
        y = snake_body[i - 1].ycor()
        snake_body[i].goto(x, y)

    # Move the head forward
    snake_body[0].forward(SNAKE_SIZE)


# ... (rest of your code)

def check_collision():
    """
    Checks for collision with the walls, food, and the snake's own body.

    Returns:
        bool: True if the game is over (collision with walls or self), False otherwise.
    """
    global score
    head = snake_body[0]

    # Wall collision
    if abs(head.xcor()) > 280 or abs(head.ycor()) > 280:
        return True

    # Food collision
    if head.distance(food) < 20:
        create_food()
        new_segment = create_turtle(*snake_body[-1].position())
        snake_body.append(new_segment)
        score += 1
        score_display.clear()
        score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

    # Self-collision (NEW)
    for segment in snake_body[1:]:  # Check all segments except the head
        if head.distance(segment) < 10:
            return True  # Game over if head touches any other segment

    return False  # No collision, game continues


# ... (rest of your code)


def reset_game():
    """
    Resets the game state.
    """
    global snake_body, food, score
    # Clear the screen
    for segment in snake_body:
        segment.goto(1000, 1000)  # Move off screen
    food.goto(1000, 1000)  # Move off screen
    # Reset the game state
    snake_body = [create_turtle(*pos) for pos in start_positions]
    food = create_food()
    score = 0
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))


def game_loop():
    """
    Main game loop.
    """
    if not check_collision():
        move_snake()
        screen.update()
        screen.ontimer(game_loop, GAME_SPEED)
    else:
        score_display.clear()
        score_display.goto(0, 0)
        score_display.write(f"Game Over! Final Score: {score}", align="center", font=("Courier", 20, "normal"))
        # Ask the player if they want to play again
        play_again = screen.textinput("Game Over", "Play again? (yes/no)").lower()
        if play_again == "yes":
            reset_game()
            game_loop()


# Setup the screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create initial snake body
start_positions = [(0, 0), (-SNAKE_SIZE, 0), (-2 * SNAKE_SIZE, 0)]
snake_body = [create_turtle(*pos) for pos in start_positions]

# Create initial food
create_food()

# Keyboard bindings
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# Display initial score
score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

# Start the game loop
game_loop()

# Keep the window open until closed by the user
screen.mainloop()
