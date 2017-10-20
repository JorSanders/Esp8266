# demo DC motor on port GPIO15
# show motor speed on OLED on I2C
# 2017-1009 PePo new OOP, assignment make it working!

import machine, time, ssd1306
import motor  #motor class

# motor object
GPIO_MOTOR = 12
motor = motor.Motor(GPIO_MOTOR)

# OLED on I2C
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
oled = ssd1306.SSD1306_I2C(128, 32, i2c)

# OLED function: erse OLED screen
def erase():
    # TODO!
    pass

# OLED function: display speed on OLED
def displaySpeed(speed, x=0, y=0):
    # TODO!
    pass


MOTOR_MIN = 0 # minimum duty - trial and error
MOTOR_MAX  = 1023 # maximum duty

# Motor function: slowly turn on the motor
def motorAccelerate(display=None, d1=MOTOR_MIN, d2=MOTOR_MAX, step=1, dt=0.01):
    for i in range(d1, d2, step):
        motor.speed(i)
        if display is not None:
            displaySpeed(motor.speed(), 0, 0)
        time.sleep(dt)

# demo
def run():
    motorAccelerate(oled, MOTOR_MIN, MOTOR_MAX, 10) # motor accelarate
    time.sleep(2) # wait 2 seconds
    # TODO!:  motorSlowDown(oled, MOTOR_MAX, MOTOR_MIN,-5)# motor slowdown
    motor.brake() # stop motor
    displaySpeed(motor.speed(), 0, 0)

# run
run()
