from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
screen = Screen()
screen.setup(width=500, height=400)
all_turtles = []
is_race_on = False

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, 120 - turtle_index * 50)
    all_turtles.append(new_turtle)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 200:
            winner = turtle.fillcolor()
            is_race_on = False
        turtle.forward(random.randint(0, 10))
if winner == user_bet:
    print("You win!")
else:
    print("You lose.")
try:
    print(f"The {winner} turtle win.")

screen.exitonclick()
