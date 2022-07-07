import turtle
turtle.shape("triangle")
turtle.pensize(2)

colorsQuantity = int(input("How many colors would you like to use?: "))
colorsList = []
for i in range(0, colorsQuantity):
    color = input("Enter a color: ")
    colorsList.append(color)

for i in range(len(colorsList)):
    turtle.color(colorsList[i],colorsList[i])
    turtle.begin_fill()

    for i in range(0, 4):
        turtle.forward(70)
        turtle.left(90)
    turtle.end_fill()

    turtle.penup()
    turtle.forward(90)
    turtle.pendown()
