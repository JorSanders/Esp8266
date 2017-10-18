# Connect the button to pin 12
# I used the Ohm resistor (brown, black, orange, gold)

# Connect the led to pin 15
# I used the Ohm resistor (red, red, brown, gold)

import machine

led = machine.Pin(15, machine.Pin.OUT)
button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    if button.value():
        led.off()
    else:
        led.on()
