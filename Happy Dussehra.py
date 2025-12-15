import numpy as np
import matplotlib.pyplot as plt

message = "Happy Dussehra"
n_letters = len(message)

# X positions for letters
x_pos = np.arange(n_letters)
# Wavy Y positions
y_pos = 0.5 + 0.2 * np.sin(x_pos)

# Festive colors
festive_colors = ['#FF6B35', '#F7931E', '#FFD23F', '#FF4757', '#FF8E53']
colors = [festive_colors[i % len(festive_colors)] for i in range(n_letters)]

# Plot
fig, ax = plt.subplots(figsize=(10, 3))
ax.set_facecolor('#ccfff4')

# Draw letters with colors + wave effect
for i, (x, y, letter, color) in enumerate(zip(x_pos, y_pos, message, colors)):
    ax.text(x, y, letter,
            fontsize=60, fontweight='bold', color=color,
            ha='center', va='center',
            rotation=np.sin(i * np.pi / n_letters) * 5)

# Random festive stars
np.random.seed(42)
ax.scatter(np.random.uniform(-1, n_letters, 50),
           np.random.uniform(0, 1, 50),
           s=np.random.uniform(10, 30, 50),
           c=np.random.choice(['#FFD700', '#FF4500'], 50),
           alpha=0.6, marker='*')

# Limits
ax.set_xlim(-0.5, n_letters - 0.5)
ax.set_ylim(0, 1.2)

plt.tight_layout()
plt.show()