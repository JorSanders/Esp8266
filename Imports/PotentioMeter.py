import machine

class PotentioMeter:
    adc = None
    max = 0
    min = 0
    top = 0

    def __init__(self):
        self.adc = machine.ADC(0)
        self.max = 836
        self.min = 3
        self.top = self.max - self.min

    def getPercentage(self):
        volts = self.adc.read()
        value = volts - self.min
        percentage = value / self.max
        if percentage > 1:
            return 1
        elif percentage < 0:
            return 0
        return percentage
