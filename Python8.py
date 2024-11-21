import turtle
turtle.Screen().bgcolor("Black")
object=turtle.Turtle()
colors=["red", "orange", "yellow", "blue", "green", "purple"]
while True:
    for x in range(200):
        object.pencolor(colors[x%len(colors)])
        object.width(x/100 + 1)
        object.forward(x)
        object.left(59)
    object.right(239)