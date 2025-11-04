import turtle

t = turtle.Turtle()
colors = ["red", "blue", "green", "orange", "purple"]

t.speed(10)

for i in range(6):
    t.color(colors[i % len(colors)])  # use modulo to avoid index error
    for _ in range(5):
        t.forward(100)
        t.right(72)
    t.right(60)

turtle.done()
print("Colorful polygon art created with turtle graphics.")