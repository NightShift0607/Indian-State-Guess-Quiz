import turtle
import pandas
user_guess = []
score = 0


screen = turtle.Screen()
# screen.setup(width=750,height=500)
screen.title("Indian States Quiz")
image = "india.gif"
screen.addshape(image)
back = turtle.Turtle()
back.shape(image)


# # used to get coordinates of screen on mouse click
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)


data = pandas.read_csv("states.csv")
states_name = data.state.to_list()


def write(state):
    state_data = data[data.state == state]
    X = int(state_data.x)
    Y = int(state_data.y)
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.goto(X,Y)
    text.write(answer_state, "center", font=('Arial', 8, 'normal'))


def state_to_learn():
    missing_states = []
    for state in states_name:
        if state not in user_guess:
            missing_states.append(state)
    missed_state = {
        "Missed State": missing_states
    }
    df = pandas.DataFrame(missed_state)
    df.to_csv("States to Learn.csv")


while len(user_guess) < 28:
    answer_state = screen.textinput(f"{score}/50 State Correct", "What's another state's name").title()
    
    if answer_state == "Exit":
        state_to_learn()
        break
    
    if answer_state in states_name:
        score += 1
        user_guess.append(answer_state)
        write(answer_state)


# turtle.mainloop()