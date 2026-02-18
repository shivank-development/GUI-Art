import numpy as np
import matplotlib.pyplot as plt

x, y = np.meshgrid(
    np.linspace(-2, 2, 600),
    np.linspace(-2, 2, 600)
)

z = np.sin(x**3 - y**3) * np.cos(x * y)

plt.imshow(z, cmap="twilight")
plt.axis("off")
plt.title("Neural Fractal Art")
plt.show()
