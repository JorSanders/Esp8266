# Connect the led to pin 15
# I used the Ohm resistor (red, red, brown, gold)

import machine
import time

led = machine.Pin(15, machine.Pin.OUT)

for i in range(10):
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)