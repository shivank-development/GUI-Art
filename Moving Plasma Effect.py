import cv2, numpy as np
import math

h, w = 400, 400
t = 0

while True:
    frame = np.zeros((h, w, 3), dtype=np.uint8)
    for y in range(h):
        for x in range(w):
            r = int((math.sin(x / 20 + t) + math.sin(y / 25 + t)) * 127 + 128)
            g = int((math.sin(x / 25 - t) + math.cos(y / 20 + t)) * 127 + 128)
            b = int((math.cos(x / 20 + t) + math.sin(y / 25 - t)) * 127 + 128)

            # Clamp to [0,255] to avoid overflow
            r = max(0, min(255, r))
            g = max(0, min(255, g))
            b = max(0, min(255, b))

            frame[y, x] = [b, g, r]

    cv2.imshow("Plasma", frame)
    t += 0.1

    # Press ESC to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
