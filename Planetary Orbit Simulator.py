import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 400)

a, b = 1, 0.6          # semi-major & semi-minor axes
x = a * np.cos(t)
y = b * np.sin(t)

plt.plot(x, y, label="Orbit")
plt.scatter([0], [0], color="orange", label="Star")

plt.title("Planet Orbit")
plt.axis("equal")
plt.legend()
plt.show()
