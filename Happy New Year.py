import turtle
import random

t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

turtle.bgcolor("#1a1a2e")

# Draw heart
t.penup()
t.goto(0, -120)
t.setheading(140)
t.pendown()

t.color("#ff4d6d", "#ff8fa3")
t.begin_fill()
t.forward(180)
t.circle(-90, 200)
t.left(120)
t.circle(-90, 200)
t.forward(180)
t.end_fill()

# Text
t.penup()
t.goto(0, -10)
t.color("khaki")
t.write(
    "By 2026, may all your dreams come true!",
    align="center",
    font=("Arial", 22, "bold")
)

# Firefly / spark dots
t.color("yellow")
for _ in range(30):
    t.penup()
    t.goto(random.randint(-250, 250), random.randint(-200, 200))
    t.dot(5)

turtle.done()
