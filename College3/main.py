import machine

led = machine.Pin(14, machine.Pin.OUT)
led.on()

from machine import UART

uart = UART(1, 115200)                         # init with given baudrate
uart.init(115200, bits=8, parity=None, stop=1) # init with given parameters

while True:
    uart.write('abc')   # write the 3 characters

led.off()
