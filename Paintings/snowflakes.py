from turtle import *
import turtle as T
from random import *


def ground():
    T.hideturtle()
    T.speed(100)
    for i in range(400):
        T.pensize(randint(5, 10))
        x = randint(-400, 350)
        y = randint(-280, -1)
        r = -y / 280
        g = -y / 280
        b = -y / 280
        T.pencolor(r, g, b)
        T.penup()
        T.goto(x, y)
        T.pendown()
        T.forward(randint(40, 100))


def snow():
    T.hideturtle()
    T.speed(100)
    T.pensize(2)
    for i in range(100):
        r = random()
        g = random()
        b = random()
        T.pencolor(r, g, b)
        T.penup()
        T.setx(randint(-350, 350))
        T.sety(randint(1, 270))
        T.pendown()
        dens = randint(8, 12)
        snowsize = randint(10, 14)
        for j in range(dens):
            T.forward(snowsize)
            T.backward(snowsize)
            T.right(360 / dens)


def main():
    T.setup(800, 600, 0, 0)
    T.tracer(False)
    T.bgcolor("black")
    snow()
    ground()
    T.tracer(True)
    T.mainloop()


main()