from turtle import Turtle, Screen
import pandas as pd
import pygame
pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('sound.wav')
t = Turtle()
screen = Screen()
screen.title('US state game')
image = 'stateguess/blank_states_img.gif'
screen.bgpic(image)
t.penup()
t.hideturtle()
data = pd.read_csv('stateguess/50_states.csv')
all_states = data.state.to_list()
inputstates=[]
while len(inputstates)<len(all_states):
    answer_state =screen.textinput(title=f'{len(inputstates)}/50 guess the state',prompt='please enter a state')
    if answer_state is None or answer_state.lower() == "exit":
        break
    answer_state = answer_state.title() 
    if answer_state in all_states and answer_state not in inputstates:
        inputstates.append(answer_state)
        state_row = data[data.state == answer_state]
        x = int(state_row.x.iloc[0])
        y = int(state_row.y.iloc[0])
        t.goto(x, y)
        t.dot(10, 'yellow')
        sound.play()
        t.write(answer_state, align="center", font=("Arial", 10, "normal"))

screen.exitonclick()