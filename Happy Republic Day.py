import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 3))
ax.axis("off")

ax.set(xlim=(0, 10), ylim=(-1, 1))
x = np.linspace(0, 10, 300)

# Tricolor waves
ax.plot(x, 0.15*np.sin(x) - 0.6, lw=10, c="#FF9933")  # Saffron
ax.plot(x, 0.15*np.sin(x) - 0.8, lw=10, c="#000000")  # Black
ax.plot(x, 0.15*np.sin(x) - 1.0, lw=10, c="#138808")  # Green

# Ashoka Chakra
t = np.linspace(0, 2*np.pi, 150)
ax.plot(1.4 + 0.25*np.cos(t), 0.25*np.sin(t), c="#0038A8", lw=2)

for a in np.linspace(0, 2*np.pi, 24):
    ax.plot(
        [1.4, 1.4 + 0.25*np.cos(a)],
        [0, 0.25*np.sin(a)],
        c="#0038A8",
        lw=1
    )

ax.text(3.2, 0, "REPUBLIC DAY", fontsize=30, weight="bold", va="center")
ax.text(3.2, -0.4, "26 January", fontsize=14, c="#0038A8", va="center")

plt.show()
