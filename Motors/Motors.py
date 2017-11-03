import machine, time
import servo, PotentioMeter

sv_pin = machine.Pin(15, machine.Pin.OUT)  # Huzzah: Servo op GPIO14
sv = servo.Servo(sv_pin)

pin_motor = machine.Pin(13, machine.Pin.OUT)
motor = machine.PWM(pin_motor)

led = machine.PWM(machine.Pin(12))
led.freq(60)

potentioMeter = PotentioMeter.PotentioMeter()

while True:
    i = potentioMeter.getPercentage()
    motor.duty((int)(i * 1023))
    led.duty((int)(i * 1023))
    sv.write_angle((int)(1 +i * 179))
    time.sleep(0.1)
