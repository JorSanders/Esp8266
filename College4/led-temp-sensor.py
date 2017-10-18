import machine, ssd1306, time

screenWidth = 128
screenHeight = 32
delay = 1
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
oled = ssd1306.SSD1306_I2C(screenWidth, screenHeight, i2c)
adc = machine.ADC(0)

while True:
    oled.fill(0)
    oled.show()
    volts = adc.read()
    temp = (volts - 500) / 10
    temp -= 5
    oled.text('Temp:', 0, 5)
    oled.text(str(temp), int(screenWidth/2), 5)
    oled.text('Volt:', 0, int(screenHeight/2))
    oled.text(str(volts), int(screenWidth/2), int(screenHeight/2))
    oled.show()
    time.sleep(delay)

