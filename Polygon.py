import turtle
turtle.Screen().bgcolor("green")
turtle.Screen().setup(400,400)

polygon = turtle.Turtle()
num_sides = int(input("Enter the number of sides: "))
side_length = 70
angle = 360.0 / num_sides
polygon.shape("turtle")

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()