FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level=1

    def update_scoreboard(self):
        self.clear()
        self.goto(0,200)
        self.write(f"Level: {self.level}", align="left", font=FONT)
    def add_point(self):
        self.level +=1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="left", font=FONT)




