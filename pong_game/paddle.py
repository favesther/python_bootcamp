from turtle import *
UP = 20
DOWN = -20

class Paddle(Turtle):
    def __init__(self, x=350, y=0):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.setposition(x, y)

    # def

    def up(self):
        new_y = self.ycor() + UP
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() + DOWN
        self.goto(self.xcor(), new_y)

