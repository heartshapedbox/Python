# Нарисуйте цифры 1, 2, 3, изображенные ниже, начиная
# от нижней точки цифры 1.

import random
import turtle
t = turtle.Turtle()
t.hideturtle()
t.pensize(2)

t.left(90)
t.forward(200)
t.penup()
t.right(90)
t.forward(100)
t.pendown()
for i in range(0, 2):
    t.forward(100)
    t.right(90)
for i in range(0, 2):
    t.forward(100)
    t.left(90)
t.forward(100)
t.penup()
t.forward(100)
t.pendown()
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)
t.left(90)
t.penup()
t.forward(100)
t.pendown()
t.left(90)
t.penup()
t.forward(30)
t.pendown()
t.forward(70)
