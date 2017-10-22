import machine

import College4.Random
from Imports import Oled

oled = Oled.Oled()
oled.erase()

robj = College4.Random.Random()
delay = 0.5
screenWidth = 128
screenHeight = 32

drawButton = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
eraseButton = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)


def drawSquare(x, y, size):
    oled.rectangle(int(x), int(y), int(size))


def drawCircle(x, y, radius):
    oled.circle(int(x), int(y), int(radius))


def drawShape(x, y, size):
    shape = robj.randRange(1)

    if shape == 0:
        drawCircle(x, y, size/1.5)
    elif shape == 1:
        drawSquare(x, y, size)


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