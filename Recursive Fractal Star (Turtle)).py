import turtle

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.color("cyan")

# Recursive star function
def star(size, depth):
    if depth == 0:
        return
    for i in range(5):
        t.forward(size)
        star(size/2, depth-1)   # recursion
        t.right(144)

# Move turtle to position
t.penup()
t.goto(-100, -50)
t.pendown()

# Draw fractal star
star(200, 3)

turtle.done()
