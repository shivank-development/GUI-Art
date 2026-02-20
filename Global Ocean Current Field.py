import numpy as np
import matplotlib.pyplot as plt

# Create grid (longitude, latitude)
x, y = np.meshgrid(
    np.linspace(-180, 180, 30),
    np.linspace(-90, 90, 15)
)

# Vector components
u = np.cos(np.radians(y))
v = np.sin(np.radians(x))

plt.figure(figsize=(10, 5))
plt.quiver(x, y, u, v)

plt.title("Global Ocean Currents")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.tight_layout()
plt.show()
