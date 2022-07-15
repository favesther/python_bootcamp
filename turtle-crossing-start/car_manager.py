from turtle import *
import random
import time


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle()
            car.shape("square")
            car.shapesize(1, 2)
            car.color(COLORS[random.randint(0, 5)])
            car.penup()
            car.goto(260, random.randint(-280, 280))
            car.setheading(180)
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            if car.xcor() < -320:
                self.all_cars.remove(car)
            else:
                car.goto(car.xcor() - self.move_distance, car.ycor())

    def speed_up(self):
        self.move_distance += MOVE_INCREMENT




