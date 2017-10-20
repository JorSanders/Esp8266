# needs ssd1306 class!!! Downloaded from
# https://github.com/adafruit/micropython-adafruit-ssd1306
import ssd1306 as lcd
import machine


class Oled(lcd.SSD1306_I2C):
    def __init__(self, width=128, height=32, i2c=machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4)), addr=0x3c,
                 external_vcc=False):
        super().__init__(width, height, i2c, addr, external_vcc)

    def erase(self, show=1):
        self.fill(0)
        if (show):
            self.show()

    def message(self, message, x=0, y=0, show=1):
        self.text(message, x, y)
        if (show):
            self.show()

    def update(self, message, x, y, show=1):
        self.rectangle(x, y, len(message) * 8, 8, 0)
        self.message(message, x, y)
        if (show):
            self.show()

    def rectangle(self, left, top, width, height=0, color=0x1, show=1):
        if height == 0:
            height = width

        xStep = 1
        if width < 0:
            xStep = -1

        yStep = 1
        if height < 0:
            yStep = -1

        for y in range(0, height, yStep):
            for x in range(0, width, xStep):
                self.pixel(left + x, top + y, color)
        if (show):
            self.show()

    def circle(self, x0, y0, r, show=1):
        for y in range(y0 - r, y0 + r + 1):
            for x in range(x0 - r, x0 + r + 1):
                xd = x - x0
                yd = y - y0
                if xd * xd + yd * yd < r * r:
                    self.pixel(x, y, 1)
        if (show):
            self.show()
