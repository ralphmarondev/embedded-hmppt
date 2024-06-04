import serial
import time 

ser = serial.Serial('COM3', 9600)
time.sleep(2)

messages = ['hello', 'how areyou', 'python and arduino']

try:
    while True:
        for message in messages:
            ser.write(message.encode())
            time.sleep(2)

except KeyboardInterrupt:
    print('Keyboard interrupt detected. Exiting...')

ser.close()


'''
diffx
- distance from camera center x and object center y
diffy
- distance from camera center y and object center y
'''