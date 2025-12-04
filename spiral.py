import turtle
turtle.Screen().setup(500,500)
loadWindow = turtle.Screen()
turtle.speed(2)

colours = [ "red", "purple", "blue", "green", "orange", "purple" ]

my_pen = turtle.Pen()
turtle.bgcolor("black")
for x in range(360):
    my_pen.pencolor(colours[x % 6])
    my_pen.width(x/100 + 1)
    my_pen.forward(x)
    my_pen.left(50)
