from turtle import *


class Scoreboard(Turtle):

    def __init__(self):
        super(Score, self).__init__()
        self.score = 0
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

