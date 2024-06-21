import turtle
from turtle import Screen, Turtle
from random import randint

class SnakeGame:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        self.screen.tracer(0)
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.high_score = self.load_high_score()
        self.score_display = Turtle()
        self.setup_score_display()
        self.setup_bindings()

    def setup_bindings(self):
        self.screen.listen()
        self.screen.onkey(self.snake.turn_up, "Up")
        self.screen.onkey(self.snake.turn_down, "Down")
        self.screen.onkey(self.snake.turn_left, "Left")
        self.screen.onkey(self.snake.turn_right, "Right")

    def setup_score_display(self):
        self.score_display.hideturtle()
        self.score_display.penup()
        self.score_display.color("white")
        self.score_display.goto(0, 260)
        self.update_score_display()

    def update_score_display(self):
        self.score_display.clear()
        self.score_display.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def load_high_score(self):
        try:
            with open("high_score.txt", "r") as file:
                return int(file.read())
        except:
            return 0

    def save_high_score(self):
        with open("high_score.txt", "w") as file:
            file.write(str(self.high_score))

    def run_game(self):
        self.screen.update()
        if not self.game_over_check():
            self.check_collision()
            self.snake.move()
            self.screen.ontimer(self.run_game, 100)

    def game_over_check(self):
        if abs(self.snake.head.xcor()) > 290 or abs(self.snake.head.ycor()) > 290:
            self.game_over()
            return True
        return False

    def check_collision(self):
        if self.snake.head.distance(self.food.instance) < 15:
            self.food.place_food()
            self.snake.extend()
            self.score += 10
            if self.score > self.high_score:
                self.high_score = self.score
                self.save_high_score()
            self.update_score_display()

    def game_over(self):
        self.snake.reset()
        self.score = 0
        self.update_score_display()
        self.ask_replay()

    def ask_replay(self):
        self.snake.hide()
        self.food.hide()
        self.screen.update()
        response = self.screen.textinput("Game Over", "Play again? (yes/no)")
        if response and response.lower() == 'yes':
            self.reset_game()
        else:
            self.screen.bye()  # Close the screen

    def reset_game(self):
        self.snake.reset()
        self.food.reset()  # Reset food to make sure it appears
        self.score = 0
        self.update_score_display()
        self.setup_bindings()
        self.run_game()

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(3):
            self.add_segment((-20 * i, 0))

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg_num - 1].xcor()
            y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x, y)
        self.head.forward(20)

    def turn_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def turn_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def turn_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def turn_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def hide(self):
        for segment in self.segments:
            segment.hideturtle()

class Food:
    def __init__(self):
        self.instance = Turtle("circle")
        self.instance.color("red")
        self.instance.penup()
        self.place_food()

    def place_food(self):
        self.instance.goto(randint(-280, 280), randint(-280, 280))

    def hide(self):
        self.instance.hideturtle()

    def reset(self):
        self.instance.showturtle()  # Ensure the food turtle is visible
        self.place_food()  # Reposition the food

if __name__ == "__main__":
    game = SnakeGame()
    game.run_game()
    game.screen.exitonclick()