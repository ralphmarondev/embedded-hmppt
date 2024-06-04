import serial
import time

# Establish serial connection with Arduino
ser = serial.Serial('COM3', 9600)  # Change 'COM3' to your Arduino's serial port
time.sleep(2)  # Allow time for the serial connection to initialize

try:
    while True:
        # Send '1' to turn the LED on
        ser.write(b'1')
        print("LED on")
        time.sleep(1)

        # Send '0' to turn the LED off
        ser.write(b'0')
        print("LED off")
        time.sleep(1)

        ser.write('Hello world, Ralph Maron Eda is here')
        time.sleep(1)
except KeyboardInterrupt:
    # Handle Ctrl+C gracefully
    print("Exiting program")
    ser.close()
