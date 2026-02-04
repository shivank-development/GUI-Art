import cv2
import time

cap = cv2.VideoCapture(0)

t0, frames = time.time(), 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    edges = cv2.Canny(frame, 120, 240)

    # FPS calculation
    frames += 1
    elapsed = time.time() - t0
    fps = frames / elapsed

    # Display FPS on frame
    cv2.putText(
        edges,
        f"FPS: {fps:.1f}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        255,
        2
    )

    cv2.imshow("Live Edge Detection", edges)

    # Press ESC to exit
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
