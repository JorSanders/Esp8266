import machine, time

red = machine.Pin(14, machine.Pin.OUT)
green = machine.Pin(12, machine.Pin.OUT)
blue = machine.Pin(13, machine.Pin.OUT)

green.on()
red.on()
blue.off()

