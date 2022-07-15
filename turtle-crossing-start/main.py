import time
from turtle import *
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
cars = CarManager()
screen.update()

screen.listen()
screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    cars.create_car()
    cars.move_cars()

    for car in cars.all_cars:
        if player.distance(car) < 30:
            game_is_on = False
            break

    if player.ycor() >= 280:
        scoreboard.update_scoreboard()
        cars.speed_up()
        player.reset_position()
    screen.update()


screen.exitonclick()
