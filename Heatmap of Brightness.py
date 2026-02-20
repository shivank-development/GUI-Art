import cv2
import numpy as np

img = cv2.imread("3.jpeg", 0)  # 0 = grayscale

if img is None:
    print("Image not found!")
else:
    heatmap = cv2.applyColorMap(img, cv2.COLORMAP_JET)

    cv2.imshow("Heatmap", heatmap)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
