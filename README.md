#right side
8  - gpio14
9  - gpio12
10 - gpio13
11 - gpio15
12 - gpio0
13 - gpio16
14 - gpio2
15 - i2c SCL
16 - i2c SDA

#left
2 - RST?
3 - 3v
4 - NC?
5 - Ground
6 - Adc in (MAX 1v!!!)

#http://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html#deploying-the-firmware
#https://askubuntu.com/questions/133235/how-do-i-allow-non-root-access-to-ttyusb0-on-12-04


#led
long leg plus
short leg grnd
red red brown gold resistor

#button
cros connect
value (0) means pressed

#servo
yellow gpo
brown grnd
red 5v (battery)
condensator between 5v line and grnd(short leg 5v, long leg grnd)

#motor
redline to diode white line of diode on the redline side
blue line on the end of that diode
connect that to middle pin of diode
right pin of the transistor to grnd
left pin a brown black orange gold resistor to ground
after resistor connect to a gpio pin

#TMP36
facing the flat side
left is grnd
right is 3v
middle is adc out

#Potentiometer
right pin grnd
middle pin adc
left pin 3x brown black orange resistor


