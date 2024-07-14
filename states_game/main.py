import turtle
import pandas as pd

STATES_DATA = "50_states.csv"
STATES = pd.read_csv(STATES_DATA)
print(STATES)
STATES_LIST = STATES["state"].to_list()
print(STATES_LIST)
IMAGE = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(IMAGE)

turtle.shape(IMAGE)


def pick_state(title, prompt):
    return screen.textinput(title=title, prompt=prompt).title()


while len(STATES_LIST) > 0:
    answer_state = pick_state("Guess the State", "What's another state's name?")

    for state in range(len(STATES_LIST)):
        if answer_state == STATES_LIST[state]:
            state_x = STATES[STATES["state"] == answer_state]["x"]
            state_y = STATES[STATES["state"] == answer_state]["y"]
            turtle.goto(int(state_x), int(state_y))
            # turtle.goto(int(STATES["x"][state]), int(STATES["y"][state]))
            turtle.write(answer_state)
            remove_state = STATES_LIST.pop(state)
            print(remove_state)
            print("Yes")
            break
screen.exitonclick()
