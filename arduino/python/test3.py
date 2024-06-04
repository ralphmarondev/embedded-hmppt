import cv2
import serial
import time 


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

ser = serial.Serial('COM3', 9600)
time.sleep(2)

def detect_and_draw_closest_head(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    heads = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))

    if len(heads) == 0:
        return None, None, None
    
    closest_head = max(heads, key=lambda r: r[2] * r[3])

    x, y, w, h = closest_head

    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    center_x = x + w // 2
    center_y = y + h // 2

    return frame, center_x, center_y

def map_value(value, left_min, left_max, right_min, right_max):
    left_span = left_max - left_min
    right_span = right_max - right_min
    value_scaled = float(value - left_min) / float(left_span)

    return right_min + (value_scaled * right_span)

def send_servo_angle(center_x, frame_width):
    servo_angle = map_value(center_x, 0, frame_width, 0, 180)
    ser.write(f'{servo_angle}\n'.encode())

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame, center_x, center_y  = detect_and_draw_closest_head(frame)

    if center_x is not None and center_y is not None:
        send_servo_angle(center_x, frame.shape[1])

    # adding check for frame dimension
    if frame is not None and frame.shape[0] > 0 and frame.shape[1] > 0:
        cv2.imshow('Frame', frame)
        print('showing') 
    else:
        print('Invalid frame dimesions')

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
ser.close()

