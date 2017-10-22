# Scripts and games for the ESP8266 in (micro)python
This are some scripts and games I made for my Esp board.
IE: Pong game, jumping game, temperature reading graph via serial connection, knightrider leds

## Prerequisites
* [Firmware](http://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html#deploying-the-firmware)
* [Ampy](https://github.com/adafruit/ampy)

To access serial connections without root permission see [this](https://askubuntu.com/questions/133235/how-do-i-allow-non-root-access-to-ttyusb0-on-12-04) fix

## Pinlayout
I pinned my ESP board on a breadboard with the MicroUSB facing up. Below i listed the breadboard lines that correspond with the ESP pins
### Right side
* 8  - gpio14
* 9  - gpio12
* 10 - gpio13
* 11 - gpio15
* 12 - gpio0
* 13 - gpio16 (no Pwm)
* 14 - gpio2
* 15 - i2c SCL
* 16 - i2c SDA

### Left side
* 3 - 3v
* 4 - NC?
* 5 - Ground
* 6 - Adc in (MAX 1v!!!)

[Full info on pinlayout](https://cdn-learn.adafruit.com/downloads/pdf/adafruit-feather-huzzah-esp8266.pdf)


## Devices
Please note that these are the devices i got in my kit. And might differ from yours. Please check before connection your own devices

###led
* Connect long leg to a gpio or any Vs
* Connect short leg to ground
* Use red red brown gold resistor (Asuming 3v is used)

###button
* cros connect (IE top left - right bottom)
* value (0) means pressed

###servo
* Connect the yellow line to a gpio port
* Connect the brown line to ground
* Connect the red line to a 5v supply. Esp doesnt have that so i used a battery pack
* Connect a condensator between 5v line and grnd(short leg 5v, long leg grnd)

###motor
* Connect the red line of the motor to diode white line of diode on the redline side
* Connect the blue line of the motor on the end of that diode
* Connect that to middle pin of a transistor
* Connect the Right pin of the transistor to ground
* Connect the left pin of the transistor with a brown black orange gold resistor to ground
* After resistor on the transistor line connect to a gpio pin

###TMP36
* Facing the flat side
* Connect the left pin to ground
* Connect the right pin is 3v supply
* Connect the middle to the Adc pin on the Esp
* With hot temperatures the Adc pin might get overloaded so expirement with resistor

#Potentiometer
* Arrow facing up
* Connect the right pin ground
* Connect the middle to the Adc pin on the Esp
* Connect the left pin with 3 times a brown black orange resistor to 3v supply

## Ampy commands
Im on a Ubuntu 16.04 my serial port = /dev/ttyUSB0 for windows is will be something like COM3

Run a file (ctrl + c doesnt stop the script from running just detaches your terminal)
```
ampy --port /dev/ttyUSB0 run test.py
```

Put a file on the board
```
ampy --port /dev/ttyUSB0 put test.py
```

Remove a file from the board
```
ampy --port /dev/ttyUSB0 rm test.py
```

List files on the board
```
ampy --port /dev/ttyUSB0 ls
```

