'''
diffx
- distance from camera center x and object center y
diffy
- distance from camera center y and object center y
'''
import cv2
import math

# Load pre-trained face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Capture video from webcam
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()

    if not ret:
        break

    # Convert frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Calculate the center of the camera's field of view
    camera_center_x = frame.shape[1] // 2
    camera_center_y = frame.shape[0] // 2

    # Find the nearest face
    nearest_face = None
    min_distance = float('inf')
    for (x, y, w, h) in faces:
        face_center_x = x + w // 2
        face_center_y = y + h // 2
        distance = ((face_center_x - camera_center_x) ** 2 + (face_center_y - camera_center_y) ** 2) ** 0.5
        if distance < min_distance:
            min_distance = distance
            nearest_face = (x, y, w, h)

    # Draw rectangle around nearest face
    if nearest_face is not None:
        x, y, w, h = nearest_face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Calculate diffx and diffy
        diffx = camera_center_x - (x + w // 2)
        diffy = camera_center_y - (y + h // 2)

        # calculate angle
        angle = math.degrees(math.atan2(diffy, diffx))

        # Display x, y coordinates and angle
        cv2.putText(frame, f'X: {x + w // 2}, Y: {y + h // 2}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(frame, f'Angle: {angle}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        # Print diffx and diffy
        print(f"diffx: {diffx}, diffy: {diffy}")

    # Display the frame
    cv2.imshow('Frame', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()
