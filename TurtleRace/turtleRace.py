import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500,height=400)
usr_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
colors=["red","green","blue","yellow","orange", "purple"]
turtle_name=[]

y_axis= -50
def teleport(name):
    global y_axis
    name.penup()
    name.goto(x=-250,y=y_axis)
    y_axis+=40

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    teleport(new_turtle)
    turtle_name.append(new_turtle)


while True:

    for turtle in turtle_name:
        if turtle.xcor()>230:
            winning_color=turtle.pencolor()
            if winning_color==usr_bet:
                print(f"You've won!, The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost!,The {winning_color} turtle is the winner.")
            exit()
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)

print(turtle_name)


screen.exitonclick()
