import turtle
turtle.Screen().bgcolor("White")
turtle.Screen().setup(400, 300)
turtle.title("Welcome to Turtle Window")

object = turtle.Turtle()
for i in range(4):
    object.forward(100)
    object.left(90)
    i = i+1

turtle.done()