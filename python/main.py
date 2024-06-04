import serial.tools.list_ports as port
import serial 

ports = port.comports()
serialInst = serial.Serial()
portsList = []

for onePort in ports:
    portsList.append(str(onePort))
    print(str(onePort))

val = input('Select Port: COM')

for x in range(0, len(portsList)):
    if portsList[x].startswith('COM' + str(val)):
        portVar = 'COM' + str(val)
        print(portVar)

serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()

while True:
    command = input("Arduino Comman: (On/OFF): ")
    serialInst.write(command.encode('utf-8'))

    if command == 'exit':
        exit()

