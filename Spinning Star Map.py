import turtle
import math

t = turtle.Turtle()
t.speed(0)

# Setup screen
s = turtle.Screen()
s.bgcolor("black")

# Draw pattern
for i in range(36):
    t.color("cyan")
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.forward(200)
    t.backward(200)
    t.right(10)

turtle.done()
