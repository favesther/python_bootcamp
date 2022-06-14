from turtle import *
starting_x, starting_y = 0, 0
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()
        self.heading = self.body[0]

    def create_snake(self):
        x = starting_x
        y = starting_y
        for _ in range(3):
            tim = Turtle(shape="square")
            tim.penup()
            tim.color("white")
            tim.setposition(x, y)
            x -= MOVE_DISTANCE
            self.body.append(tim)

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].goto(self.body[i - 1].pos())
        if abs(self.body[0].xcor()) >= 250 or abs(self.body[0].ycor()) >= 250:
            self.body[0].left(90)
        self.body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.body[0].heading() != DOWN:  # can't go back directly
            self.body[0].setheading(UP)

    def down(self):
        if self.body[0].heading() != UP:
            self.body[0].setheading(DOWN)

    def left(self):
        if self.body[0].heading() != RIGHT:
            self.body[0].setheading(LEFT)

    def right(self):
        if self.body[0].heading() != LEFT:
            self.body[0].setheading(RIGHT)

    def add_segment(self):
        tim = Turtle(shape="square")
        tim.penup()
        tim.color("white")
        tim.setposition(x, y)
        x -= MOVE_DISTANCE
        self.body.append(tim)