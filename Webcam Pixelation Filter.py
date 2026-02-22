import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize down
    small = cv2.resize(frame, (32, 32), interpolation=cv2.INTER_LINEAR)

    # Resize up (pixelated effect)
    pixelated = cv2.resize(
        small,
        (frame.shape[1], frame.shape[0]),
        interpolation=cv2.INTER_NEAREST
    )

    cv2.imshow("Pixelated Webcam", pixelated)

    # Press ESC to exit
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
