from turtle import Turtle


class Player:
    def __init__(self):
        self.player = Turtle()
        self.create_turtle()

    def create_turtle(self):
        self.player.shape("turtle")
        self.player.color("black")
        self.player.penup()
        self.player.goto(0, -280)
        self.player.setheading(90)

    def move_up(self):
        new_y = self.player.ycor() + 10
        self.player.goto(self.player.xcor(), new_y)




