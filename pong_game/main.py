from turtle import *
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)
right_paddle = Paddle()
left_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = ScoreBoard()
screen.update()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)

    if abs(ball.ycor()) > 270:
        ball.bounce()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.turnaround()
        time.sleep(ball.move_speed)
        scoreboard.right_addpoint()

    if ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.turnaround()
        time.sleep(ball.move_speed)
        scoreboard.left_addpoint()

    # right side
    if ball.xcor() > 380:
        scoreboard.left_addpoint()
        ball.reset_position()

    # left side
    if ball.xcor() < -380:
        scoreboard.right_addpoint()
        ball.reset_position()

    ball.move()

    screen.update()

screen.exitonclick()
