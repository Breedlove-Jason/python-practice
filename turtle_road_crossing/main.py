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
        self.car_manager = Cars()

        for _ in range(difficulty_level()):
            self.car_manager.draw_car()

        self.screen.onkey(self.player.move_up, "Up")
        self.screen.listen()

        self.game_loop()
        self.screen.mainloop()

    def game_loop(self):
        for car in self.car_manager.all_cars:
            move_car(car)
            if self.car_manager.collision(self.player):
                print("collision")
            else:
                continue
        self.screen.update()
        self.screen.ontimer(self.game_loop, 1)


if __name__ == "__main__":
    Main()
