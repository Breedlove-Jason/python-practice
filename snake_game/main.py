from turtle import Turtle, Screen
from random import randint

snake_body = []


def turtle_maker(x, y):
    """Creates a new turtle segment at the given x, y position."""
    new_turtle = Turtle()
    new_turtle.shape("square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.goto(x, y)
    return new_turtle


def food_maker():
    """Creates a new food turtle at a random position."""
    food = Turtle()
    food.shape("circle")
    food.color("red")
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
    """Moves the snake forward by updating the position of each segment."""
    screen.listen()
    screen.onkey(move_up, "Up")
    screen.onkey(move_down, "Down")
    screen.onkey(move_left, "Left")
    screen.onkey(move_right, "Right")

    # Move the segments from tail to head
    for i in range(len(snake_body) - 1, 0, -1):
        x = snake_body[i - 1].xcor()
        y = snake_body[i - 1].ycor()
        snake_body[i].goto(x, y)

    # Move the head forward
    snake_body[0].forward(20)


def check_collision():
    """Checks for collision with the walls."""
    head = snake_body[0]
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        return True
    return False


def game_loop():
    """Main game loop."""
    if not check_collision():
        move_snake()
        screen.update()
        screen.ontimer(game_loop, 100)
    else:
        print("Game Over!")
        screen.bye()


# Setup the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create initial snake body
start_positions = [(0, 0), (-20, 0), (-40, 0)]
for position in start_positions:
    snake_body.append(turtle_maker(*position))

# Start the game
game_is_on = True
game_loop()

screen.exitonclick()
