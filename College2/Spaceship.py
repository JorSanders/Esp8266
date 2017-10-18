# Connect the button to pin 14
# I used the Ohm resistor (brown, black, orange, gold)

# Connect the leds to pin 13, 12, 15
# I used the Ohm resistor (red, red, brown, gold) for each led

import machine
import time

ledGreen = machine.Pin(13, machine.Pin.OUT)
ledRed1 = machine.Pin(12, machine.Pin.OUT)
ledRed2 = machine.Pin(15, machine.Pin.OUT)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
delay = 0.3

while True:
    if button.value():
        ledGreen.on()
        ledRed1.off()
        ledRed2.off()
    else:
        ledRed2.on()
        ledGreen.off()
        ledRed1.off()

        time.sleep(delay)

        ledGreen.on()
        ledRed2.off()

        time.sleep(delay)

        ledRed1.on()
        ledGreen.off()

        time.sleep(delay)

