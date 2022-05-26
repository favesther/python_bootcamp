from turtle import *
import random

colormode(255)


def draw_duobianxing(n):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    pencolor((r, g, b))
    for _ in range(n):
        left(360/n)
        forward(100)


# for i in range(3, 11):
#     draw_duobianxing(i)


def random_walk():
    while True:
        # r = random.randint(0, 255)
        # g = random.randint(0, 255)
        # b = random.randint(0, 255)
        for r in range(0, 255, 30):
            for g in range(0, 255, 30):
                for b in range(0, 255, 30):
                    pencolor((r, g, b))
                    pensize(5)
                    angle = random.choice([0, 90, 180, 270])
                    # angle = random.randint(0, 360)
                    forward(20)
                    setheading(angle)

# random_walk()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def circles(size_of_gap):
    speed("fastest")
    for angle in range(0, 360, size_of_gap):
        setheading(angle)
        pencolor(random_color())
        circle(100)
    done()



circles(5)