import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
pencil = turtle.Turtle()
pencil.hideturtle()
game_is_on = True
data = pd.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []

while game_is_on and len(guessed_states) < 50:
    answer_state = screen.textinput(
        f"{len(guessed_states)}/50 States Correct", "What's another state name?").title()
    if answer_state == "Exit":
        missing_states = [
            state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state = data[data["state"] == answer_state]
        coordinate = (int(state["x"]), int(state["y"]))
        pencil.penup()
        pencil.goto(coordinate)
        pencil.pendown()
        pencil.write(answer_state)
