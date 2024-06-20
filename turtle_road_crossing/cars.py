import random
from turtle import Turtle

NUMBER_OF_CARS = 10


class Cars:
    def __init__(self):
        self.colors = ['red', 'blue', 'green', 'yellow', "orange", "purple", "black", "silver", "gold"]
        # self.difficulty_level()

    # def difficulty_level(self):
    #     level = input(f"Enter a difficulty to begin: Level 1, 2, 3")
    #     return NUMBER_OF_CARS * level

    def get_color(self):
        return random.choice(self.colors)

    def draw_car(self):
        car = Turtle()
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(self.get_color())
        car.penup()
        car.goto(random.randint(-300, 300), random.randint(-300, 300))
        return car

    def move_car(self, car):
        car.forward(10)
        if car.xcor() > 300:
            car.goto(-300, random.randint(-300, 300))
        return car
