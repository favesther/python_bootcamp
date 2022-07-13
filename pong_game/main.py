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
    print(ball.distance(paddle))
    if abs(ball.ycor()) > 280:
        ball.bounce()
    if ball.distance(paddle) < 30:
        ball.turnaround()
    if abs(ball.xcor()) > 350:
        game_is_on = False
        print("GAME OVER")
    ball.move()
        # screen.write("GAME OVER", align=ALIGNMENT, font=FONT)
    screen.update()
    time.sleep(0.1)

screen.exitonclick()
