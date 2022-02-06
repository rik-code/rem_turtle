from turtle import *
import turtle as t
from random import *


def ground():
    t.hideturtle()
    t.speed(100)
    for i in range(400):
        t.pensize(randint(5, 10))
        x = randint(-400, 350)
        y = randint(-280, -1)
        r = -y / 280
        g = -y / 280
        b = -y / 280
        t.pencolor(r, g, b)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.forward(randint(40, 100))


def snow():
    t.hideturtle()
    t.speed(100)
    t.pensize(2)
    for i in range(100):
        r = random()
        g = random()
        b = random()
        t.pencolor(r, g, b)
        t.penup()
        t.setx(randint(-350, 350))
        t.sety(randint(1, 270))
        t.pendown()
        dens = randint(8, 12)
        snowsize = randint(10, 14)
        for j in range(dens):
            t.forward(snowsize)
            t.backward(snowsize)
            t.right(360 / dens)


def main():
    t.setup(800, 600, 0, 0)
    t.tracer(False)
    t.bgcolor("black")
    snow()
    ground()
    t.tracer(True)
    t.mainloop()


main()