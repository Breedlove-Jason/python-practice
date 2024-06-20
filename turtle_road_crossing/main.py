from turtle import Screen
from cars import Cars
class Main:
    def __init__(self):
        screen = Screen()
        screen.listen()
        screen.setup(width=600, height=600)
        screen.title("Turtle Crossing")
        screen.tracer(0)

        cars = Cars()
        for _ in range(10):
            cars.draw_car()
            screen.update()
            cars.move_car()
            screen.update()
        screen.exitonclick()

if __name__ == "__main__":
    Main()