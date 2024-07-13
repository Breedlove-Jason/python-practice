import turtle

IMAGE = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(IMAGE)

turtle.shape(IMAGE)

with open("50_states.csv") as file:
    data = file.readlines()
    states = [state.strip() for state in data]


answer_state = screen.textinput(
    title="Guess the State", prompt="What's another state's name?"
).title()
print(answer_state)
