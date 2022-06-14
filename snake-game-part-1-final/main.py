# from turtle import Screen
from turtle import *
import time
from Snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    snake.move()
    screen.update()
    time.sleep(0.5)
    if snake.body[0].distance(food) < 15:
        snake.body.append()
        food.refresh()
    # TODO.1 detect collision

screen.exitonclick()
