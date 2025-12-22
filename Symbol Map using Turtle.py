import turtle
import random

t = turtle.Turtle()
t.speed(0)  # fastest drawing
screen = turtle.Screen()
screen.bgcolor("black")

colors = ["cyan", "magenta", "yellow", "white"]

for _ in range(50):
    t.penup()
    t.goto(random.randint(-200, 200), random.randint(-200, 200))
    t.pendown()
    
    t.color(random.choice(colors))
    for _ in range(4):
        t.forward(50)
        t.right(90)

turtle.done()