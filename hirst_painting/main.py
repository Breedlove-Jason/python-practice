import colorgram
from turtle import Turtle, Screen
from random import choice

# Number of colors to extract from the image
NUM_COLORS = 10

# Extract colors from the image
colors = colorgram.extract('hirst_painting.jpg', NUM_COLORS)

# Convert Color objects to RGB tuples
rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

# Setup Turtle and Screen
turtle = Turtle()
screen = Screen()
screen.colormode(255)
screen.setup(600, 600)
turtle.penup()
turtle.hideturtle()


def draw_spots(colors):
    """Draw a grid of colored dots on the screen."""
    num_dots = 10
    window_width = screen.window_width()
    window_height = screen.window_height()
    dot_distance = window_width / num_dots
    start_x = -window_width / 2 + dot_distance / 2
    start_y = window_height / 2 - dot_distance / 2

    for row in range(num_dots):
        for col in range(num_dots):
            random_color = choice(colors)
            turtle.setpos(start_x + col * dot_distance, start_y - row * dot_distance)
            turtle.dot(20, random_color)


# Draw the dots and keep the window open
draw_spots(rgb_colors)
screen.exitonclick()
