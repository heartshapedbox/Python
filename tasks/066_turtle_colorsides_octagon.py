# Нарисуйте восьмиугольник, все стороны которого окрашены в разные
# цвета (случайно выбираемые из списка шести возможных цветов).

import random
import turtle
t = turtle.Turtle()
t.hideturtle()
t.pensize(2)

colors = ["red","yellow","orange","blue","green","pink"]

for i in range(0, 8):
    randomColor = random.choice(colors)
    turtle.color(randomColor)
    turtle.forward(100)
    turtle.left(45)
