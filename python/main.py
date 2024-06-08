import serial
import time 


ser = serial.Serial(port='COM4', baudrate=9600, timeout=1)
time.sleep(2)

def send_data(data):
    ser.write(bytes(data, 'utf-8'))
    time.sleep(0.1)
    data = ser.readline()
    return data

while True: 
    n = input('Enter number: ')
    send_data(n)

ser.close()