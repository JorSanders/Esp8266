import machine
import ssd1306
import urandom

PIXEL_WIDTH = 64
PIXEL_HEIGHT = 32
MAX_BRIGHT = 100
screenWidth = 128
screenHeight = 32
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
oled = ssd1306.SSD1306_I2C(screenWidth, screenHeight, i2c)

while True:
    for x in range(PIXEL_WIDTH):
        for y in range(PIXEL_HEIGHT):
            oled.pixel(x, y, urandom.getrandbits(2))

    oled.show()
