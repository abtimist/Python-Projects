import random
from turtle import Turtle, Screen, colormode
tim = Turtle()
colormode(255)
class color():
    def randomColor(self):
        r= random.randint(1,255)
        g= random.randint(1,255)
        b= random.randint(1,255)
        return tim.pencolor((r,g,b))
class spinograph():

    def draw(self,usr_input):
        c = color()
        for i in range(int(360/usr_input)):
            tim.speed("fastest")
            c.randomColor()
            tim.circle(100)
            tim.right(i)
        Screen().exitonclick()


start = spinograph()
start.draw(5)


