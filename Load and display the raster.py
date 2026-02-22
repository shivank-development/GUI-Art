import rasterio
import matplotlib.pyplot as plt

with rasterio.open("georeferenced_raster.tif") as src:
    band = src.read(1)

plt.figure(figsize=(6, 6))
plt.imshow(band, cmap="gray")
plt.title("Demo Raster")
plt.colorbar(label="Pixel Value")
plt.axis("off")
plt.show()
