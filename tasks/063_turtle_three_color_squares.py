# Нарисуйте в один ряд
# три квадрата, разделенных промежутками.
# Заполните их тремя разными цветами.

import random
import turtle
t = turtle.Turtle()
t.hideturtle()
t.pensize(2)

colors = ["lime","yellow","cyan","magenta","green","blue"]
count = 0
while count < 3:
    randColor1 = random.choice(colors)
    randColor2 = random.choice(colors)
    t.color(randColor1, randColor2)
    t.begin_fill()
    for i in range(0, 4):
        t.forward(100)
        t.left(90)
    t.end_fill()
    t.penup()
    t.forward(125)
    t.pendown()
    count += 1
