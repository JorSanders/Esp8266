import machine

led = machine.PWM(machine.Pin(0))

# how manytimes per second
led.freq(60)
# power on 1024 is max
led.duty(1024)

