from PIL import Image
import matplotlib.pyplot as plt

# Load & shrink image for faster color analysis
img = Image.open("photo.jpg").resize((20, 20))

# Get colors (count, color)
colors = img.getcolors(400)

# Take top 5 colors
top_colors = colors[:5]
sizes = [c[0] for c in top_colors]
labels = [str(c[1]) for c in top_colors]

# Plot pie chart
plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Top 5 Dominant Colors")

plt.show()
