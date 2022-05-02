# Нарисуйте узор, который меняется при
# каждом запуске программы. Используйте
# функцию random для выбора количества
# линий, длины каждой линии и каждого угла
# поворота.

import random
import turtle
t = turtle.Turtle()
t.hideturtle()
t.pensize(2)

steps = random.randint(5, 25)

for i in range(0, steps):
    randomLength = random.randint(20, 101)
    randomAngle = random.randint(1, 361)
    t.forward(randomLength)
    t.right(randomAngle)
