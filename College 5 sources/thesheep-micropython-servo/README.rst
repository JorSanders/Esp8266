A Micropython Library for Hobby Servo Control for ESP8266
*********************************************************

This is a simple class for controlling hobby servos with Micropython on the
ESP8266 boards. It's in fact a simple convenience wrapper over the
``machine.PWM`` functionality.

Currently, the supported pins are 0, 2, 4, 5, 12, 13, 14, 15 -- because only
those pins are supported by ``machine.PWM``. Pins 1 and 3 may become supported
in the future.

To use this library, simply copy it to the ESP8266's filesystem, or include
it in the ``scripts`` directory while compiling the Micropython firmware.
