import math
import time

import machine

import ssd1306

PIXEL_WIDTH = 20
PIXEL_HEIGHT = 20
MAX_BRIGHT=100
screenWidth = 128
screenHeight = 32
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
oled = ssd1306.SSD1306_I2C(screenWidth, screenHeight, i2c)

while True:
    current = time.time()
    for x in range(PIXEL_WIDTH):
        for y in range(PIXEL_HEIGHT):
            v = math.sin(x+current)
            v += math.sin(1.0*(x*math.sin(current/0.5)+y*math.cos(current/0.25))+current)
            cx = x + 0.5*math.sin(current/5.0)
            cy = y + 0.5*math.cos(current/3.0)
            v += math.sin(math.sqrt((math.pow(cx, 2.0)+math.pow(cy, 2.0))+1.0)+current)
            v = (v+3.0)/6.0
            r = math.sin(v*math.pi)
            a = int(MAX_BRIGHT*r)
            if a > 80:
                oled.pixel(x, y , 1)
            else:
                oled.pixel(x, y, 0)
    oled.show()
