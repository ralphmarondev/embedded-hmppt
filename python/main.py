import serial
import time 

arduino_port = '/dev/ttyACM0'
baud_rate = 9600

ser = serial.Serial(arduino_port, baud_rate, timeout=1)
time.sleep(2)

def send_data(data):
    ser.write(data.encode())
    time.sleep(0.1)
    
send_data('A')
send_data('B')

ser.close()

