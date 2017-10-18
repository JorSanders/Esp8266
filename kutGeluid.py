import machine
import time
pwm = machine.PWM(machine.Pin(15))

while True:
    pwm.freq(60)
    pwm.duty(1000)
    time.sleep(0.5)
    pwm.freq(0)
    pwm.duty(0)
    break