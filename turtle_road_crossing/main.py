from turtle import Screen
from cars import Cars, move_car, difficulty_level
from player import Player


class Main:
    def __init__(self):
        screen = Screen()
        screen.listen()
        screen.setup(width=600, height=600)
        screen.title("Turtle Crossing")
        screen.tracer(0)

        cars = Cars()
        car_list = []
        for i in range(difficulty_level()):
            cars = Cars()
            car = cars.draw_car()
            car_list.append(car)
            screen.update()

        while True:
            [move_car(car)for car in car_list]

            screen.update()
        screen.exitonclick()

        player = Player()
        player.create_turtle()


if __name__ == "__main__":
    Main()
