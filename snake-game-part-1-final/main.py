# from turtle import Screen
from turtle import *
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
# screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

body = []
x, y = 0, 0
for _ in range(2):
    tim = Turtle()
    # tim.color("white", "white")
    # tim.shape("square")
    x -= 10
    tim.setposition(x, y)
    body.append(tim)


# snake = Snake()
# food = Food()
#
# screen.listen()
# screen.onkey(snake.up, "Up")
# screen.onkey(snake.down, "Down")
# screen.onkey(snake.left, "Left")
# screen.onkey(snake.right, "Right")
#
# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#
#     snake.move()
#
#
screen.exitonclick()