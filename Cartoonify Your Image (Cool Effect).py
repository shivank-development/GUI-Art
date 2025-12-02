import cv2

# Read image
img = cv2.imread("dog.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply median blur
blur = cv2.medianBlur(gray, 5)

# Edge detection using adaptive threshold
edges = cv2.adaptiveThreshold(
    blur,
    255,
    cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY,
    9,
    9
)

# Bilateral filter for smooth colors
color = cv2.bilateralFilter(img, 10, 250, 250)

# Combine edges with color image
cartoon = cv2.bitwise_and(color, color, mask=edges)

# Show result
cv2.imshow("Cartoon Image", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
