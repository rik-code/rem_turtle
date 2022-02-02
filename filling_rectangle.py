import turtle

t = turtle.Turtle()

# Adding fill
t.fillcolor('blue')
# Begin fill
t.begin_fill()

t.forward(50)
t.right(90)
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(100)
# End fill
t.end_fill()

turtle.done()