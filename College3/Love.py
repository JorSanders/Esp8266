import machine
import ssd1306
import time

screenWidth = 128
screenHeight = 32
delay = 1
ledGreen = machine.Pin(14, machine.Pin.OUT)
ledYellow = machine.Pin(12, machine.Pin.OUT)
ledRed = machine.Pin(13, machine.Pin.OUT)
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
oled = ssd1306.SSD1306_I2C(screenWidth, screenHeight, i2c)
adc = machine.ADC(0)
baseTemp = 21.5
step = 1

def showLove(temp):
    ledGreen.off()
    ledYellow.off()
    ledRed.off()
    if temp > baseTemp:
        ledGreen.on()
    if temp > baseTemp + step:
        ledYellow.on()
    if(temp > baseTemp + step*2):
        ledRed.on()

def printTemp(temp):
    oled.text('Temp:', 0, 5)
    oled.text(str(temp), int(screenWidth/2), 5)
    oled.text('Volt:', 0, int(screenHeight/2))
    oled.text(str(volts), int(screenWidth/2), int(screenHeight/2))
    oled.show()

while True:
    oled.fill(0)
    oled.show()
    volts = adc.read()
    temp = (volts - 500) / 10
    temp -= 5

    showLove(temp)
    printTemp(temp)
    time.sleep(delay)

