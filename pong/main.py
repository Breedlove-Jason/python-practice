from turtle import Turtle, Screen
import random

score1 = 0
score2 = 0

paddle1 = Turtle()
paddle2 = Turtle()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pong Game")
screen.listen()

draw_ball = Turtle()
draw_ball.shape("square")
draw_ball.color("white")
draw_ball.penup()
draw_ball.goto(0, 0)


def create_paddle(paddle, x, y):
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.penup()
    paddle.goto(x, y)


def move_up(paddle):
    y = paddle.ycor()
    y += 20
    paddle.sety(y)


def move_down(paddle):
    y = paddle.ycor()
    y -= 20
    paddle.sety(y)


def update_score():
    scoreboard = Turtle()
    scoreboard.color("white")
    scoreboard.penup()
    scoreboard.hideturtle()
    scoreboard.goto(0, 260)

    scoreboard.clear()
    scoreboard.write("{}  {}".format(score1, score2), align="center",
                     font=("Courier", 24, "normal"))
    screen.update()


def draw_center_line():
    center_line = Turtle()
    center_line.color("white")
    center_line.penup()
    center_line.goto(0, 300)
    center_line.setheading(270)
    for _ in range(15):
        center_line.pendown()
        center_line.forward(20)
        center_line.penup()
        center_line.forward(20)
    screen.update()


def move_ball():
    x = draw_ball.xcor()
    y = draw_ball.ycor()
    x += 1
    y += 1
    draw_ball.goto(x, y)
    screen.update()


direction = 1  # 1 for up, -1 for down


def computer_move_paddle(paddle):
    global direction
    y = paddle.ycor()
    y += direction
    paddle.sety(y)
    screen.update()
    if paddle.ycor() >= 250:
        direction = -1
    elif paddle.ycor() <= -250:
        direction = 1


update_score()
draw_center_line()
create_paddle(paddle1, 280, 0)
create_paddle(paddle2, -280, 0)
screen.update()

while True:
    screen.onkeypress(lambda: move_up(paddle2), "Up")
    screen.onkeypress(lambda: move_down(paddle2), "Down")
    screen.update()
    move_ball()
    screen.update()
    computer_move_paddle(paddle1)
    screen.update()
screen.mainloop()
screen.exitonclick()
