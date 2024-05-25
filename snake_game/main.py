from turtle import Turtle, Screen

snake_body = []


def turtle_maker(x, y):
    new_turtle = Turtle()
    new_turtle.shape("square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.goto(x, y)
    return new_turtle


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
    screen.listen()
    screen.onkey(move_up, "Up")
    screen.onkey(move_down, "Down")
    screen.onkey(move_left, "Left")
    screen.onkey(move_right, "Right")
    for turtle_num in range(len(snake_body) - 1, 0, -1):
        new_x = snake_body[turtle_num - 1].xcor()
        new_y = snake_body[turtle_num - 1].ycor()
        snake_body[turtle_num].goto(new_x, new_y)

    snake_body[0].forward(20)


def game_over():
    global game_is_on
    # Detect collision with wall
    if (snake_body[0].xcor() > 280 or snake_body[0].xcor() < -280 or snake_body[0].ycor() > 280
            or snake_body[0].ycor() < -280):
        game_is_on = False

    game_is_on = False


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

start_positions = [(0, 0), (-20, 0), (-40, 0)]  # For 3 initial turtle objects
for position in start_positions:
    snake_body.append(turtle_maker(*position))

game_is_on = True
while game_is_on:
    screen.update()
    move_snake()
    game_over()

    screen.update()
screen.update()
screen.exitonclick()
