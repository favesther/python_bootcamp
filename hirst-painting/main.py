###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
from turtle import *
import random
ht()    # hide turtle
colormode(255)
penup()

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
number_of_dots = 100
x = -200
y = -200
radius = 20
setpos(x, y)

for color in colors:
    rgb_colors.append(color.rgb)

i = 0
for _ in range(number_of_dots//10):
    for _ in range(10):
        color = random.choice(rgb_colors)
        pendown()
        dot(radius, (color.r, color.g, color.b))
        penup()
        forward(radius*2)
        i += 1

    y += radius*2
    setpos(x, y)

done()

