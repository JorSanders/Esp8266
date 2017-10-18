import serial
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=None, xonxoff=False, rtscts=False, dsrdtr=False) #Tried with and without the last 3 parameters, and also at 1Mbps, same happens.
#ser.flushInput()
#ser.flushOutput()
while True:
    bytesToRead = ser.inWaiting()
    ser.read(bytesToRead)