import numpy as np
import matplotlib.pyplot as plt

# Generate random steps (-1 or +1) for both X and Y
steps = np.random.choice([-1, 1], size=(2, 1000))

# Compute cumulative sum to get positions
pos = np.cumsum(steps, axis=1)

# Plot the random walk
plt.plot(pos[0], pos[1], color='lime')

plt.axis('off')
plt.title("Random Walk Visualization", color='lime', fontsize=14)
plt.show()
plt.style.use('dark_background')  # Use a dark background for better contrast