import serial.tools.list_ports

def send_data(string_to_send: str):
    serialInst = serial.Serial()

    serialInst.baudrate = 9600
    serialInst.port = 'COM4'
    serialInst.open()

    command = string_to_send
    serialInst.write(command.encode('utf-8'))
