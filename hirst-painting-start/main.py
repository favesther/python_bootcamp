###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
from turtle import *
colormode(255)
penup()

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
x = -50
y = -50
radius = 30
setpos(x, y)

for color in colors:
    rgb_colors.append(color.rgb)

i = 0
for _ in range(5):
    for _ in range(6):
        color = rgb_colors[i]
        pendown()
        dot(radius, (color.r, color.g, color.b))
        penup()
        forward(radius*2)
        i += 1

    y += radius*2
    setpos(x, y)


print(rgb_colors)

