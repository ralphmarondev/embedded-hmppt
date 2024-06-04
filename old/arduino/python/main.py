import cv2
import serial
import time
import numpy as np

# Set up the serial connection to the Arduino
ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with your Arduino's COM port
time.sleep(2)  # Wait for the serial connection to initialize

# Initialize the camera
cap = cv2.VideoCapture(0)

# Define the range for hand color in HSV
lower_skin = np.array([0, 20, 70], dtype=np.uint8)
upper_skin = np.array([20, 255, 255], dtype=np.uint8)

# Initialize state variable
hand_detected = False

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Flip the frame to avoid mirror image
        frame = cv2.flip(frame, 1)
        
        # Convert the frame to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Create a binary mask where white represents the hand
        mask = cv2.inRange(hsv, lower_skin, upper_skin)
        
        # Apply some morphological operations to remove noise
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        
        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            if cv2.contourArea(largest_contour) > 1000:  # Adjust the threshold value as needed
                if not hand_detected:
                    ser.write(b'1')  # Send signal to make the LED blink
                    hand_detected = True
                # Optionally, you can draw the contour for debugging
                cv2.drawContours(frame, [largest_contour], -1, (0, 255, 0), 3)
            else:
                if hand_detected:
                    ser.write(b'0')  # Send signal to turn off the LED
                    hand_detected = False
        else:
            if hand_detected:
                ser.write(b'0')  # Send signal to turn off the LED
                hand_detected = False
        
        # Display the mask and the frame
        cv2.imshow('Mask', mask)
        cv2.imshow('Frame', frame)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # Turn off the LED
    ser.write(b'0')
    time.sleep(1)  # Give Arduino some time to process the signal
    # Release resources
    cap.release()
    cv2.destroyAllWindows()
    ser.close()
