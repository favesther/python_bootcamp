from turtle import *

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.color("black")
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="LEFT", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="CENTER", font=("Courier", 30, "bold"))

