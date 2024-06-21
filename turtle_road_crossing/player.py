from turtle import Turtle, Screen


class Player:
    def __init__(self):
        self.player = None
        screen = Screen()
        screen.listen()
        screen.setup(width=600, height=600)
        screen.title("Turtle Crossing")
        screen.tracer(0)

    def create_turtle(self):
        self.player = Turtle()
        self.player.pendown()
        self.player.color("black")
        self.player.shape("turtle")
        self.player.penup()
        self.player.goto(0, 0)

player = Player()
player.create_turtle()
screen = Screen()
screen.update()
screen.exitonclick()



