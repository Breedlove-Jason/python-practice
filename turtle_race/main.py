from turtle import Turtle, Screen
from random import shuffle

colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
shuffle(colors)

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
NUM_TURTLES = 5
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")

tim = Turtle()
jim = Turtle()
jason = Turtle()
brandon = Turtle()
shawnda = Turtle()

vertical_spacer = 50
total_turtle_space = NUM_TURTLES * vertical_spacer
starting_y = SCREEN_HEIGHT / 2 - total_turtle_space / 2
turtles = [tim, jim, jason, brandon, shawnda]
num_turtles = len(turtles)
for index, turtle in enumerate(turtles):
    x = -200
    y = starting_y - (index * vertical_spacer)
    turtle.penup()
    turtle.goto(x, y + 40)
    turtle.shape('turtle')

    turtle.color(colors[index])

screen.exitonclick()
