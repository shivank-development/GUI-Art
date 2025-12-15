from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.cluster import KMeans

# Load image using Pillow
img = Image.open('w23.jpg').convert('RGB')

# Also load with matplotlib for processing
image = mpimg.imread('w23.jpg')
w, h, d = image.shape

# Reshape to a list of pixels
pixels = image.reshape(w * h, d)

# Number of colors to extract
n_colors = 10

# Apply KMeans clustering
kmeans = KMeans(n_clusters=n_colors, random_state=42, n_init=10).fit(pixels)

# Extract color palette
palette = np.uint8(kmeans.cluster_centers_)

# Show color palette as a horizontal bar
plt.figure(figsize=(8, 2))
plt.imshow([palette])
plt.axis('off')
plt.title("Extracted Color Palette")
plt.show()
