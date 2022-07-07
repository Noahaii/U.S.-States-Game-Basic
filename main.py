import turtle as t
import pandas as pd

#set up screen
screen = t.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

answer = screen.textinput("Guess a State", "What is a state").title()
while len(guessed_states) < 50:
    if answer == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        missing_df = pd.DataFrame(missing_states)
        missing_df.to_csv("states_to_learn.csv")
        break
    if answer in all_states:
        answer_data = data[data.state == answer]
        answer_xcor = int(answer_data.x)
        answer_ycor = int(answer_data.y)
        player_answer = t.Turtle()
        player_answer.penup()
        player_answer.goto(answer_xcor, answer_ycor)
        player_answer.hideturtle()
        player_answer.write(arg=answer)
        if answer not in guessed_states:
            guessed_states.append(answer)
    answer = screen.textinput(f"{len(guessed_states)}/50 States", "What is another state").title()
t.mainloop()