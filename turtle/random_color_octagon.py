import turtle
import random

turtle.pensize(2)
turtle.shape("circle")

sides = ["red","yellow","orange","blue","green","pink"]

for i in range(0, 8):
    randomSide = random.choice(sides)
    turtle.color(randomSide)
    turtle.forward(100)
    turtle.left(45)
