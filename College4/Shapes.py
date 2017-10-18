import Oled
import Random
import machine

oled = Oled.Oled()
oled.erase()

robj = Random.Random()
delay = 0.5
screenWidth = 128
screenHeight = 32

drawButton = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
eraseButton = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)


def drawSquare(x, y, size):
    oled.rectangle(x, y, size)


def drawCircle(x, y, radius):
    oled.circle(x, y, radius)


def drawShape(x, y, radius):
    shape = robj.randRange(1)

    if shape == 0:
        drawCircle(x, y, size)
    elif shape == 1:
        drawSquare(x, y, size/2)


while True:
    size = robj.randRange(15, 3)
    x = robj.randRange(screenWidth)
    y = robj.randRange(screenHeight)

    if drawButton.value():
        drawButtonLifted = 1
    elif drawButtonLifted:
        drawButtonLifted = 0
        drawShape(x, y, size)

    if not eraseButton.value():
        oled.erase()