from turtle import Screen
from cars import Cars, move_car, difficulty_level
from player import Player


class Main:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.title("Turtle Crossing")
        self.screen.tracer(0)
        self.player = Player()

        self.cars = []
        for _ in range(difficulty_level()):
            car = Cars().draw_car()
            self.cars.append(car)

        self.screen.onkey(self.player.move_up, "Up")
        self.screen.listen()

        self.game_loop()
        self.screen.mainloop()

    def game_loop(self):
        for car in self.cars:
            move_car(car)
        self.screen.update()
        self.screen.ontimer(self.game_loop, 100)


if __name__ == "__main__":
    Main()
