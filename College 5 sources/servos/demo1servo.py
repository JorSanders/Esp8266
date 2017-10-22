# demo#1 servo motor: showing PWM
# servo is connected to GPIO14
# 2017-1008 PePo demo for college #5

import machine, time
import servo
# Notice: module servo.py on Smartworld >> SmartDevices
# It's a modified servo module from DiCola: extended with deinit()

# create servo object - default arguments
sv_pin = machine.Pin(16, machine.Pin.OUT) #Huzzah: Servo op GPIO14
sv = servo.Servo(sv_pin)
time.sleep(1)

# sweep servo between 0 en 180 degrees, and back
try:
    while True:
        sv.write_angle(0)
        time.sleep(2)
        sv.write_angle(180)
        time.sleep(2)
except:
  sv.deinit()
  print('done!')
