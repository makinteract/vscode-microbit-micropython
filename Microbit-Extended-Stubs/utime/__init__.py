# utime

""" The utime module provides functions for getting the current 
time and date, measuring time intervals, and for delays.

Note
The utime module is a MicroPython implementation of the standard 
Python time module."""

# Functions

def sleep(seconds):
    """ Sleep for the given number of seconds. You can use a floating-point 
    number to sleep for a fractional number of seconds, or use the utime.
    sleep_ms() and utime.sleep_us() functions. """
    pass

def sleep_ms(ms):
    """ Delay for given number of milliseconds, should be positive or 0. """
    pass

def sleep_us(us):
    """ Delay for given number of microseconds, should be positive or 0. """
    pass

def ticks_ms():
    """ Returns an increasing millisecond counter with an arbitrary 
    reference point, that wraps around after some value. """
    pass

def ticks_us():
    """ Just like utime.ticks_ms() above, but in microseconds. """
    pass

def ticks_add(ticks, delta):
    """ Offset ticks value by a given number, which can be either positive 
    or negative. Given a ticks value, this function allows to calculate 
    ticks value delta ticks before or after it, following 
    modular-arithmetic definition of tick values. """
    pass