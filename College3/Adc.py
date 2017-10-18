# Very import connect everything as i described or you are gonna short wire things
# refer to https://learn.adafruit.com/micropython-hardware-analog-i-o?view=all 

# Connect the 3 volts output of your ESP to the bottom ADC pin with 22k Ohm in between
# Since i don't have a single 22k Ohm resistor i used two 10k and two 1k Ohm resistors
# 2x (brown, black, orange, gold) 2x (brown, black red, gold)
# Where the 3volts connects to the ADC also connect one 10k Ohm resistor to the ground
# (brown, black, orange)

# Connect the middle pin of the ADC to the ADC pin on your ESP

# Connect the top pin of the ADC to the ground on your ESP



import machine

adc = machine.ADC(0)

while True:
    adc.read()