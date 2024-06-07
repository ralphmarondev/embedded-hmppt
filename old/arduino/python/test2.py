'''
this is working, however, not yet tried the servo motor.
also, the frame is so big. 
'''

import cv2
import serial
import time

arduino = serial.Serial('COM3', 9600)
time.sleep(2)

cap = cv2.VideoCapture(0)

while True:
    ret, frame  = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        largest_countour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_countour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        center_x = x+w //2

        angle = int((center_x / frame.shape[1]) * 180)
        arduino.write(f'{angle}]n'.encode())

    # display the resulting frame
    cv2.imshow('Frame', frame)

    # break
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()

