import time
import serial
import matplotlib.pyplot as plt

# Stuff for the plot
plt.ion()

# Create a serial connection
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=115200,
)

# Check if serial connection is made
if not ser.isOpen():
    print ('cant connect to serial device')
    exit()

# import machine on the serial device and init the adc reader
ser.write('import machine \r\n'.encode())
ser.write('adc = machine.ADC(0) \r\n'.encode())
time.sleep(1)
ser.flushInput()

for x in range(1, 1000):
    # perform adc.read(), ignore the first line we retrieve
    # Then save the value from the second line
    ser.write('adc.read() \r\n'.encode())

    # Wait a second then read the volts
    time.sleep(1)
    unImportant = ser.readline()

    # Calculate the temp
    volts = int(ser.readline())
    temp = (volts - 500) / 10
    temp -= 5

    # Create a dot, then pause to show the plot
    plt.scatter(x,volts)
    plt.pause(0.001)

plt.pause(5)
