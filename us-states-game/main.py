import turtle
import pandas
from numpy.ma.core import size

#screen setting
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.penup()

#Creating a turtle object to display names guessed correctly.
tim = turtle.Turtle()
tim.hideturtle()
tim.penup()

#To read data in csv.
data = pandas.read_csv("50_states.csv")
states =  data.set_index("state")

#Creating game attributes
game_is_on = True
score =  0
guessed_states = []
states_not_guessed =[]
while game_is_on:

    #Exit if all states are guessed.
    if score==50:
        tim.goto(0,0)
        tim.write("Congratulations, You Guessed it all!!",align="center",font=("Arial",28,"normal"))
        break

    #Take in guesses.
    answer_state = screen.textinput(title="Guess the State", prompt=f"What's another state's name? {score}/50").title()

    #Manual exit program + A csv file of states not guessed
    if answer_state=="Exit":
        tim.goto(0, 0)
        tim.write(f"You only guessed {score}/50. ", align="center", font=("Arial", 28, "normal"))
        for i in states.index:
            if i not in guessed_states:
               states_not_guessed.append(i)
        exit_data = pandas.DataFrame(states_not_guessed)
        exit_data.to_csv("states_to learn")
        break

    #To avoid displaying already guessed word.
    if answer_state not in guessed_states:
        if answer_state in states.index:
            x_position = states.at[answer_state, "x"]
            y_position = states.at[answer_state, "y"]
            tim.goto(x_position, y_position)
            tim.write(answer_state)
            guessed_states.append(answer_state)
            score+=1


turtle.mainloop()