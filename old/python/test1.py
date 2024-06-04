import cv2
import numpy as np

# Initialize camera
camera = cv2.VideoCapture(0)

# Load pre-trained Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Camera parameters (adjust these according to your camera and setup)
known_width = 16  # Width of the object in centimeters (e.g., average width of a human head)
focal_length = 615  # Focal length of the camera in pixels (you need to calibrate this value)

file_path = "location.txt" # print output location for use of other files

def sendFileToCache(xCoords, yCoords):
    f = open(file_path, 'w')
    f.write(f'{xCoords}\n')
    f.write(f'{yCoords}\n')
    f.close()


while True:
    # Capture frame-by-frame
    ret, frame = camera.read()
    
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Find nearest face
    nearest_face = None
    min_distance = float('inf')
    for (x, y, w, h) in faces:
        # Calculate distance using face size
        face_width = w
        distance = (known_width * focal_length) / face_width
        if distance < min_distance:
            min_distance = distance
            nearest_face = (x, y, w, h)
    
    # Draw rectangle around nearest face
    if nearest_face is not None:
        (x, y, w, h) = nearest_face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # Calculate angle
        frame_height, frame_width, _ = frame.shape
        center_x = frame_width // 2
        center_y = frame_height // 2
        objCenter_x = x + w/2
        objCenter_y = y + h/2
        angle = np.arctan2(objCenter_y - center_y, objCenter_x - center_x) * (180 / np.pi)
        
        # Print information
        cv2.putText(frame, f'X: {x}, Y: {y}, Angle: {angle:.2f} degrees, Distance: {min_distance:.2f} cm', 
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        diffX = objCenter_x - center_x
        diffY = objCenter_y - center_y
    
    # Display the resulting frame
    cv2.imshow('Frame', frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Send location to cache file
    if (diffX is not None) and (diffY is not None):
        sendFileToCache(diffX, diffY)

    


# Release the camera and close all windows
camera.release()
cv2.destroyAllWindows()
