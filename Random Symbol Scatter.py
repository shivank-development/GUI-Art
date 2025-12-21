import tkinter as tk
import random

root = tk.Tk()
root.title("AI_Particles")

canvas = tk.Canvas(root, width=500, height=500, bg="black")
canvas.pack()

symbols = ["", "@paagle_badshsh", "$money", "%", "&", "*", "+", "Lavi"]

# Create 50 random particles: [x, y, dx, dy]
particles = [
    [random.randint(0, 500), random.randint(0, 500),
     random.randint(-2, 2), random.randint(-2, 2)]
    for _ in range(50)
]

def update():
    canvas.delete("all")
    for p in particles:
        # Update position
        p[0] += p[2]
        p[1] += p[3]

        # Bounce on edges
        if p[0] < 0 or p[0] > 500:
            p[2] *= -1
        if p[1] < 0 or p[1] > 500:
            p[3] *= -1

        # Draw particle
        canvas.create_text(
            p[0], p[1],
            text=random.choice(symbols),
            fill="cyan",
            font=("Courier", 16, "bold")
        )

    root.after(50, update)

update()
root.mainloop()
