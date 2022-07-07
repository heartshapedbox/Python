import random
import turtle
t = turtle.Turtle()
t.hideturtle()
t.pensize(3)
def square():
    t.begin_fill()
    for i in range(0, 4):
        t.forward(80)
        t.left(90)
    t.end_fill()
    t.penup()
    t.forward(80)
    t.pendown()
def triangle():
    t.begin_fill()
    for i in range(0, 3):
        t.forward(80)
        t.left(120)
    t.end_fill()
    t.penup()
    t.forward(80)
    t.pendown()
def circle():
    t.penup()
    t.forward(40)
    t.pendown()
    t.begin_fill()
    t.circle(40)
    t.end_fill()
    t.penup()
    t.forward(40)
    t.pendown()
def star():
    t.penup()
    t.left(90)
    t.forward(50)
    t.right(90)
    t.pendown()
    t.begin_fill()
    for i in range(0, 5):
        t.forward(80)
        t.right(144)
    t.end_fill()
    t.penup()
    t.forward(80)
    t.right(90)
    t.forward(50)
    t.left(90)

colorsList = ["aliceblue","antiquewhite","aqua","aquamarine","azure","beige","bisque","black","blanchedalmond","blue","blueviolet","brown","burlywood","cadetblue","chartreuse","chocolate","coral","cornflowerblue","cornsilk","crimson","cyan","darkblue","darkcyan","darkgoldenrod","darkgray","darkgreen","darkgrey","darkkhaki","darkmagenta","darkolivegreen","darkorange","darkorchid","darkred","darksalmon","darkseagreen","darkslateblue","darkslategray","darkslategrey","darkturquoise","darkviolet","deeppink","deepskyblue","dimgray","dimgrey","dodgerblue","firebrick","floralwhite","forestgreen","fuchsia","gainsboro","ghostwhite","gold","goldenrod","gray","green","greenyellow","grey","honeydew","hotpink","indianred","indigo","ivory","khaki","lavender","lavenderblush","lawngreen","lemonchiffon","lightblue","lightcoral","lightcyan","lightgoldenrodyellow","lightgray","lightgreen","lightgrey","lightpink","lightsalmon","lightseagreen","lightskyblue","lightslategray","lightslategrey","lightsteelblue","lightyellow","lime","limegreen","linen","magenta","maroon","mediumaquamarine","mediumblue","mediumorchid","mediumpurple","mediumseagreen","mediumslateblue","mediumspringgreen","mediumturquoise","mediumvioletred","midnightblue","mintcream","mistyrose","moccasin","navajowhite","navy","oldlace","olive","olivedrab","orange","orangered","orchid","palegoldenrod","palegreen","paleturquoise","palevioletred","papayawhip","peachpuff","peru","pink","plum","powderblue","purple","red","rosybrown","royalblue","saddlebrown","salmon","sandybrown","seagreen","seashell","sienna","silver","skyblue","slateblue","slategray","slategrey","snow","springgreen","steelblue","tan","teal","thistle","tomato","turquoise","violet","wheat","white","whitesmoke","yellow","yellowgreen","black","silver","gray","white","maroon","red","purple","fuchsia","green","lime","olive","yellow","navy","blue","teal","aqua","pink","lightpink","hotpink","deeppink","palevioletred","mediumvioletred","lavender","thistle","plum","orchid","violet","fuchsia","magenta","mediumorchid","darkorchid","darkviolet","blueviolet","darkmagenta","purple","mediumpurple","mediumslateblue","slateblue","darkslateblue","rebeccapurple","indigo","lightsalmon","salmon","darksalmon","lightcoral","indianred","crimson","red","firebrick","darkred","orange","darkorange","coral","tomato","orangered","gold","yellow","lightyellow","lemonchiffon","lightgoldenrodyellow","papayawhip","moccasin","peachpuff","palegoldenrod","khaki","darkkhaki","greenyellow","chartreuse","lawngreen","lime","limegreen","palegreen","lightgreen","mediumspringgreen","springgreen","mediumseagreen","seagreen","forestgreen","green","darkgreen","yellowgreen","olivedrab","darkolivegreen","mediumaquamarine","darkseagreen","lightseagreen","darkcyan","teal","aqua","cyan","lightcyan","paleturquoise","aquamarine","turquoise","mediumturquoise","darkturquoise","cadetblue","steelblue","lightsteelblue","lightblue","powderblue","lightskyblue","skyblue","cornflowerblue","deepskyblue","dodgerblue","royalblue","blue","mediumblue","darkblue","navy","midnightblue","cornsilk","blanchedalmond","bisque","navajowhite","wheat","burlywood","tan","rosybrown","sandybrown","goldenrod","darkgoldenrod","peru","chocolate","olive","saddlebrown","sienna","brown","maroon","white","snow","honeydew","mintcream","azure","aliceblue","ghostwhite","whitesmoke","seashell","beige","oldlace","floralwhite","ivory","antiquewhite","linen","lavenderblush","mistyrose","gainsboro","lightgray","silver","darkgray","dimgray","gray","lightslategray","slategray","darkslategray","black"]
figureList = ["circle","triangle","square","star"]
randomColorsList = []

figuresQuantityInput = int(input("How many figures would you like to print?: "))
colorsQuantityInput = int(input("How many colors would you like to use?: "))

for i in range(0, colorsQuantityInput):
    randomColor = random.choice(colorsList)
    randomColorsList.append(randomColor)

t.penup()
t.backward(600)
t.left(90)
t.forward(350)
t.right(90)
t.pendown()

figuresQuantityCountTotal = 0
figuresQuantityCountPerLine = 0
while figuresQuantityCountTotal < figuresQuantityInput:
    if figuresQuantityCountPerLine < 11:
        randomColorPen = random.choice(randomColorsList)
        randomColorFill = random.choice(randomColorsList)
        randomFigure = random.choice(figureList)
        t.color(randomColorPen,randomColorFill)

        if randomFigure == "square":
            square()
        elif randomFigure == "triangle":
            triangle()
        elif randomFigure == "star":
            star()
        else:
            circle()
        figuresQuantityCountTotal += 1
        figuresQuantityCountPerLine += 1
        t.penup()
        t.forward(25)
        t.pendown()
    else:
        t.penup()
        t.right(90)
        t.forward(90)
        t.right(90)
        t.forward(1155)
        t.right(180)
        t.pendown()
        figuresQuantityCountPerLine = 0
