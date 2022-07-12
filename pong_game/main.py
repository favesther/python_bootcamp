from turtle import *
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)
paddle = Paddle()
paddle_fixed = Paddle(-350, 0)
ball = Ball()
screen.update()

screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    print(ball.position())
    if ball.xcor() < -100 or ball.xcor() > 100 or ball.ycor() < -280 or ball.ycor() > 280:
        print(ball.heading())
        ball.bounce()
        print(ball.heading())
    screen.update()
    time.sleep(0.5)

screen.exitonclick()
