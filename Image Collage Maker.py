import cv2
import numpy as np

# Read and resize images
a = cv2.imread("1.jpeg"); a = cv2.resize(a, (300, 300))
b = cv2.imread("2.jpeg"); b = cv2.resize(b, (300, 300))
c = cv2.imread("3.jpeg"); c = cv2.resize(c, (300, 300))
d = cv2.imread("4.jpeg"); d = cv2.resize(d, (300, 300))

# Combine into collage
top = np.hstack((a, b))
bottom = np.hstack((c, d))
collage = np.vstack((top, bottom))

# Display and save collage
cv2.imshow("Collage", collage)
cv2.imwrite("collage.jpg", collage)

cv2.waitKey(0)     # ✅ Correct function name and argument
cv2.destroyAllWindows()
