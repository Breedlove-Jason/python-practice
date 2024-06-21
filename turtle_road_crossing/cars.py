import random
from turtle import Turtle

NUMBER_OF_CARS = 5


def move_car(car):
    car.forward(0.5)
    if car.xcor() > 300:
        car.goto(-300, random.randint(-290, 290))


def difficulty_level():
    while True:
        try:
            level = int(input("Enter a difficulty to begin: Level 1, 2, 3: "))
            if level in [1, 2, 3]:
                return NUMBER_OF_CARS * level
            else:
                print("Invalid level. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")


class Cars:
    def __init__(self):
        self.colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'black', 'silver', 'gold', 'cyan', 'magenta', 'brown', 'pink', 'gray', 'lime', 'olive', 'maroon', 'navy', 'teal', 'indigo']
        self.car_positions = []

    def get_color(self):
        return random.choice(self.colors)

    def draw_car(self):
        car = Turtle()
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2.5)
        car.color(self.get_color())
        car.penup()

        new_position = (random.randint(-295, 295), random.randint(-295, 295))
        while new_position in self.car_positions:
            new_position = (random.randint(-295, 295), random.randint(-295, 295))
        self.car_positions.append(new_position)
        car.goto(new_position)
        return car
