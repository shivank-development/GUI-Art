import cv2

# Initialize video capture
video_cap = cv2.VideoCapture(0)

# Load a pre-trained Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, video_data = video_cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(video_data, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the frame with detected faces
    cv2.imshow("Video Live", video_data)

    # Exit on pressing 'a'
    if cv2.waitKey(10) & 0xFF == ord('a'):
        break

# Release the video capture object and close any open windows
video_cap.release()
cv2.destroyAllWindows()
