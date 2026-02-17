from turtle import *
import random

speed(0)
bgcolor("black")

pensize(3)
up()
goto(0, -120)
down()
color("green")

# Tree body
for i in range(50):
    circle(180)
    left(7)

# Function to draw triangle decorations
def tri(a):
    seth(a)
    begin_fill()
    fd(120)
    rt(120)
    fd(120)
    rt(120)
    fd(120)
    end_fill()

# Top decoration
color("red")
up()
goto(0, 140)
down()
begin_fill()
circle(30)
end_fill()

# Triangles
for a in (160, 20):
    tri(a)

# Decorative balls
spots = [
    (140, 40), (-140, 20), (120, -60),
    (-60, -120), (100, 110), (-100, 110)
]

for x, y in spots:
    up()
    goto(x, y)
    down()
    color(random.choice(["yellow", "red"]))
    begin_fill()
    circle(15)
    end_fill()

# Greeting text
up()
goto(-160, 240)
color("white")
write("MERRY CHRISTMAS", font=("Arial", 22, "bold"))

hideturtle()
done()
