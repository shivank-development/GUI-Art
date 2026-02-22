import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 400)

plt.figure(figsize=(6, 6))

# Orbit circle
plt.plot(np.cos(theta), np.sin(theta))

# Key points
plt.scatter([0, 1, -1], [0, 0, 0], c="orange")

# Labels
plt.text(0, 0, "Sun", ha="center", va="center")
plt.text(1, 0, "Earth", ha="left", va="bottom")
plt.text(-1, 0, "L1", ha="right", va="bottom")

plt.axis("equal")
plt.axis("off")
plt.title("Simplified Orbital Diagram")

plt.show()
