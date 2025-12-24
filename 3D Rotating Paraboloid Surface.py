import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create data
x = np.linspace(-3, 3, 50)
y = np.linspace(-3, 3, 50)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

# Create figure
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Animation loop
for angle in range(0, 360, 3):
    ax.clear()
    ax.plot_surface(X, Y, Z, cmap="viridis")
    ax.view_init(elev=30, azim=angle)
    ax.set_title("3D Paraboloid Surface")
    plt.pause(0.05)

plt.show()
