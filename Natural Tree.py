import turtle
import random

t = turtle.Turtle()
screen = turtle.Screen()
t.left(90)
t.speed(0)
t.color("brown")
t.width(8)

def draw_tree(branch_length):
    if branch_length > 10:
        t.forward(branch_length)

        angle = random.randint(15, 30)
        shrink = random.randint(10, 15)

        t.right(angle)
        draw_tree(branch_length - shrink)

        t.left(angle * 2)
        draw_tree(branch_length - shrink)

        t.right(angle)
        t.backward(branch_length)

draw_tree(80)
screen.mainloop()