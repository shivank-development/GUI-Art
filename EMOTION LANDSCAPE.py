import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 300)
y = np.linspace(-3, 3, 300)

X, Y = np.meshgrid(x, y)
Z = np.sin(X**2 + Y**2)

plt.figure(figsize=(6, 6))
plt.imshow(Z, cmap="coolwarm", extent=[-3, 3, -3, 3])
plt.colorbar(label="Emotion Intensity")
plt.axis("off")
plt.tight_layout()
plt.show()
