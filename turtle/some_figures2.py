import turtle
import random

t = turtle.Turtle()
t.pensize(2)
t.hideturtle()

colorsList = ["yellow","orange","green","red","pink","black","cyan","magenta","purple","violet"]

def octagon():
    for i in range(0, 8):
        randomColor = random.choice(colorsList)
        t.color(randomColor)
        t.forward(50)
        t.left(45)
    t.left(35)


for i in range(0, 10):
    octagon()
