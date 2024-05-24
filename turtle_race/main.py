from turtle import Turtle, Screen
from random import shuffle, randint

# Constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
NUM_TURTLES = 6
COLORS = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
FINISH_LINE_OFFSET = 30
VERTICAL_SPACER = 50

# Shuffle colors for randomness
shuffle(COLORS)

# Setup screen
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

# Get user's bet
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")

# Initialize turtles
turtles = [Turtle(shape='turtle') for _ in range(NUM_TURTLES)]
starting_y = SCREEN_HEIGHT / 2 - (NUM_TURTLES * VERTICAL_SPACER) / 2 + 40


def setup_turtle(turtle, color, index):
    """Setup turtle position and color."""
    x = -SCREEN_WIDTH / 2 + 20
    y = starting_y - index * VERTICAL_SPACER
    turtle.penup()
    turtle.goto(x, y)
    turtle.color(color)


# Setup turtles
for index, turtle in enumerate(turtles):
    setup_turtle(turtle, COLORS[index], index)


def draw_finish_line():
    """Draw the finish line on the screen."""
    finish_line = Turtle()
    finish_line.penup()
    finish_line.goto(SCREEN_WIDTH / 2 - FINISH_LINE_OFFSET, -SCREEN_HEIGHT / 2)
    finish_line.setheading(90)
    finish_line.pensize(7)
    finish_line.color('red')
    finish_line.pendown()
    finish_line.forward(SCREEN_HEIGHT)
    finish_line.hideturtle()


# Draw the finish line
draw_finish_line()

# Start the race
is_race_on = bool(user_bet)

while is_race_on:
    for turtle in turtles:
        random_distance = randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() >= SCREEN_WIDTH / 2 - FINISH_LINE_OFFSET:
            winning_color = turtle.color()[0]
            print(f"The {winning_color} turtle won!")
            if winning_color == user_bet:
                print("You won!")
            else:
                print("You lost!")
            is_race_on = False
            break

screen.exitonclick()
