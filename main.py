import turtle
import pandas

# Background screen of United States
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Getting our states data
data = pandas.read_csv("50_states.csv")
state = data["state"].to_list()

ALIGNMENT = "left"
FONT = ("arial", 8, "normal")

correct_guess = 0
guessed_states = []

def write_answer(answered_state):
    coordinates = data[data.state == answered_state]
    x = coordinates.x[state.index(answered_state)]
    y = coordinates.y[state.index(answered_state)]
    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()
    writer.goto(x, y)
    writer.write(f"{answered_state}", align=ALIGNMENT, font=FONT)


while correct_guess != 50:
    answer = screen.textinput(title=f"{correct_guess}/50 States Correct", prompt="What's another state's name?")
    answer = answer.title()

    if answer == "Exit":
        missed_states = [missed_state for missed_state in state if missed_state not in guessed_states]
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer in state:
        write_answer(answer)
        guessed_states.append(answer)
        correct_guess += 1