import turtle

s=turtle.getscreen()
t=turtle.Turtle()
t.shape("classic")
t.pencolor("magenta")


for i in range(len([1] * 18)):
    t.begin_fill()
    t.fillcolor("magenta")
    t.right(90)
    t.forward(90)
    t.right(90)
    t.forward(90)
    t.right(90)
    t.forward(90)
    t.right(90)
    t.forward(90)
    t.end_fill()
    t.right(20)

turtle.exitonclick()
