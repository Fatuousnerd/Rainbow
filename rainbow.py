import turtle
colors = ['red', 'orange','white','indigo','green','pink']
pen = turtle.Pen()
turtle.bgcolor("black")
for x in range(360):
    pen.pencolor(colors[x%6])
    pen.width(x//100 + 1)
    pen.forward(x)
    pen.left(59)