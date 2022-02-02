import turtle

t = turtle.Turtle()

# Adding line thickness
t.pensize(5)

t.fillcolor('blue')

t.begin_fill()
t.forward(50)
t.right(90)
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(100)
t.end_fill()

turtle.done()