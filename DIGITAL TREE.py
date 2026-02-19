import matplotlib.pyplot as plt
import math

def branch(x, y, length, angle):
    if length < 5:
        return

    x2 = x + length * math.cos(angle)
    y2 = y + length * math.sin(angle)

    plt.plot([x, x2], [y, y2], "brown")

    branch(x2, y2, length * 0.7, angle + 0.5)
    branch(x2, y2, length * 0.7, angle - 0.5)

plt.figure(figsize=(6, 8))
branch(0, 0, 60, math.pi / 2)

plt.axis("off")
plt.show()


#Wind effect
#branch(x2, y2, length * 0.7, angle + 0.5 + random.uniform(-0.1, 0.1))
