from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,x,y):
        super().__init__()
        self.setpos(x,y)
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)

    def go_up(self):
        if self.ycor()<280:
            self.goto(self.xcor(),self.ycor() + 20)

    def go_down(self):
        if self.ycor() > -280:
            self.goto(self.xcor(),self.ycor()-20)


