from turtle import Turtle, Screen
import random

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


create_paddle(paddle1, 280, 0)
create_paddle(paddle2, -280, 0)
screen.update()

# while True:
#     screen.onkeypress(lambda: move_up(paddle2), "Up")
#     screen.onkeypress(lambda: move_down(paddle2), "Down")
#     screen.update()
screen.exitonclick()
