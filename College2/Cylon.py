import machine, time

# Set the led ports
ledports = [14,12,13,15,0,16]

#create the empty led list
leds = []

#fill the led list
for ledport in ledports:
    leds.append(machine.Pin(ledport, machine.Pin.OUT))

#turn off all leds
for led in leds:
    led.off()


i = 0 # currently burning led
UP = 1 # constant for direction upwards
DOWN = 0 # constant for direction downwards
direction = UP # variable that keeps track of direction
previous = [0,0] # light that priviously burned

while True:
    # turn the ligths on/off
    leds[i].on()
    leds[previous[0]].off()

    # update the privous list
    j = len(previous) -2
    while j >= 0:
        previous[j + 1] = previous[j]
        j -= 1
    previous[0] = i

    # check which light should burn next
    if direction == UP:
        if i >= len(leds) -1:
            direction = DOWN
            i -= 1
        else:
            i += 1
    else:
        if i <= 0:
            direction = UP
            i += 1
        else:
            i -= 1

    time.sleep(0.05)