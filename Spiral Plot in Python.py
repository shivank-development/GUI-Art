import matplotlib.pyplot as plt
import numpy as np

# Generate 100 angle values between 0 and 4π
theta = np.linspace(0, 4 * np.pi, 100)

# Define the radius as a function of theta (r = θ^1.5)
r = theta ** 1.5

# Create a polar plot
plt.polar(theta, r, color='magenta', linewidth=2)

# Add title
plt.title("Spiral Plot")

# Display the plot
plt.show()
