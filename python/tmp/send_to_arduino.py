import serial
import time 

ser = serial.Serial('COM3', 9600)
time.sleep()

value1 = 123
value2 = 456
value3 = 789

ser.write(str(value1).encode())
ser.write(b',') # separate values with a comma

ser.write(str(value2).encode())
ser.write(b',') # separate values with a comma

ser.write(str(value3).encode())
ser.write(b',') # separate values with a comma

ser.close()
