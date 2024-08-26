import turtle
from turtle import Turtle, Screen
import pandas

turtle_shape_file = "blank_states_img.gif"
csv_file_name = "50_states.csv"

screen = Screen()
screen.title("U.S. States game")
screen.register_shape(turtle_shape_file)
turtle.shape(turtle_shape_file)

df = pandas.read_csv(csv_file_name)
print(df)

entered_states = []


def show_state(data):
    st_turtle = Turtle()
    st_turtle.penup()
    st_turtle.hideturtle()
    st_turtle.goto(data[1], data[2])
    st_turtle.write(data[0])
    print(data)


while len(entered_states) < 50:
    # title = "Guess the state" if len(entered_states) < 1 else f"{len(entered_states)}/50 are guessed"
    user_answer = screen.textinput(
        "Guess the state" if len(entered_states) < 1 else f"{len(entered_states)}/50 are guessed",
        "What's another state name?").strip().title()
    print(user_answer)
    if len(df[df.state == user_answer]) > 0 and user_answer not in entered_states:
        show_state(df[df.state == user_answer].values[0].tolist())
        entered_states.append(user_answer)

screen.mainloop()
# screen.exitonclick()
