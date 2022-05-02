# Нарисуйте пятиконечную звезду.

import turtle
t = turtle.Turtle()
t.hideturtle()
t.pensize(2)

for i in range(0, 5):
    t.forward(100)
    t.right(144)
