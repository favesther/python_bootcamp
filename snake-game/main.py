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
    time.sleep(0.1)
    # TODO.2 HIT WALL
    if abs(snake.body[0].xcor()) >= 280 or abs(snake.body[0].ycor()) >= 280:
        scoreboard.reset()
        snake.reset()

    # TODO.1 detect collision
    if snake.body[0].distance(food) < 15:
        # TODO.3 eat and longer
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # TODO.4 detect collision with the tail
    for body in snake.body[1:]:
        if snake.body[0].distance(body) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
