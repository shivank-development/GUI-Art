import matplotlib.pyplot as plt
import random

# Generate random mouse points
x = [random.randint(0, 100) for _ in range(200)]
y = [random.randint(0, 100) for _ in range(200)]

# Create heatmap
plt.hexbin(x, y, gridsize=20, cmap="inferno")
plt.colorbar(label="Density")
plt.title("Mouse Heatmap")

plt.show()
