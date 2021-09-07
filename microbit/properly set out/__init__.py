"""Joseph Fergusson, 2019"""

from Image import _Image

class _Button():
    """Physical button on the Microbit board"""

    def is_pressed(self):
        """Returns True if the button is being pressed"""
        return True
    
    def was_pressed(self):
        """Returns True if the button has been pressed since this was last called"""
        return True
    
    def get_presses(self):
        """Returns the number of times the button has been pressed since this method was last called, then resets the count"""
        return 10

    def __init__(self):
        a = 0

class _Buttons():
    """Holder of the buttons"""
    def __init__(self):
        self.button_a = _Button()
        self.button_b = _Button()

class _MicroBitDigitalPin:
    """Digital pin on the Micro:Bit board"""

    def read_digital(self):
        """Return 1 if the pin is high, and 0 if it's low"""
        return 1
    
    
    def write_digital(self,value):
        """Set the pin to High if the value is 1, or else set it to 0"""
        a = value

    def __init__(self):
        a = 0

class _MicroBitAnalogDigitalPin(_MicroBitDigitalPin):
    """Analog (PWM) pin on the Micro:Bit board"""

    def read_analog(self):
        """Reads the voltage applied to the pin, and return it as an integer between 0 (0V), and 1024 (3.3V)"""
        return 1023
    
    
    def write_analog(self,value):
        """Output a PWM signal on the pin, with a duty cycle proportional to provided value, where 0 = 0%, and 1023 = 100%"""
        a = value
    
    
    def set_analog_period(self,period):
        """Set the period of the PWM signal being output to period in ms. Minimum valid is 1ms"""
        a = period
    
    
    def set_analog_period_microseconds(self,period):
        """Set the period of the PWM signal being output to period in microseconds. Minimum valid is 256"""
        a = period
    
    def __init__(self):
        a = 0

class _MicroBitTouchPin(_MicroBitAnalogDigitalPin):
    """Touch sensitive pin on the Micro:Bit board"""

    def is_touched(self):
        """Return True if the pin is being touched, otherwise False"""
        return True

    def __init__(self):
        a = 0

class _MicroBitAnalogDigitalPinReadOnly:
    """Read only PWM pin"""

    def read_analog(self):
        """Reads the voltage applied to the pin, and return it as an integer between 0 (0V), and 1024 (3.3V)"""
        return 1023
    
    def __init__(self):
        a = 0

def panic(self, error_code):
    """Enter a panic mode. Requires restart. Pass in an arbitrary integer <= 255 to indicate a status"""
    s = error_code

def reset(self):
    """Restart the board."""
    a = 0

def sleep(self,milliseconds):
    """Wait for n milliseconds. One second is 1000 milliseconds, so:"""
    a = milliseconds

def running_time(self):
    """Return the number of milliseconds since the board was switched on or restarted."""
    return 10

def temperature(self):
    """Return the temperature of the micro:bit in degrees Celcius."""
    return 26.2

button_a = _Button
button_b = _Button

pin0 = _MicroBitTouchPin()
pin1 = _MicroBitTouchPin()
pin2 = _MicroBitTouchPin()

pin3 = _MicroBitAnalogDigitalPin()
pin4 = _MicroBitAnalogDigitalPin()
pin5 = _MicroBitDigitalPin()
pin6 = _MicroBitDigitalPin()
pin7 = _MicroBitDigitalPin()
pin8 = _MicroBitDigitalPin()
pin9 = _MicroBitDigitalPin()

pin10 = _MicroBitAnalogDigitalPin()

pin11 = _MicroBitDigitalPin()
pin12 = _MicroBitAnalogDigitalPin()
pin13 = _MicroBitDigitalPin()
pin14 = _MicroBitDigitalPin()
pin15 = _MicroBitDigitalPin()
pin16 = _MicroBitDigitalPin()

pin19 = _MicroBitDigitalPin()
pin20 = _MicroBitDigitalPin()

"""Image stuff"""
def Image(string = None, width=None, height=None, buffer=None):
    """Image() - Create a blank 5x5 image
Image(string) - Create an image by parsing the string, a single character returns that glyph
Image(width, height) - Create a blank image of given size
Image(width, height, buffer) - Create an image from the given buffer"""
    return _Image()
