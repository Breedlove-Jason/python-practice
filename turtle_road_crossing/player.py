from turtle import Turtle


class Player:
    def __init__(self):
        self.turtle = Turtle()
        self.create_turtle()

    def create_turtle(self):
        self.turtle.shape("turtle")
        self.turtle.color("black")
        self.turtle.penup()
        self.turtle.goto(0, -280)
        self.turtle.setheading(90)

    def move_up(self):
        new_y = self.turtle.ycor() + 10
        self.turtle.goto(self.turtle.xcor(), new_y)
