#NeoPixel

""" The neopixel module lets you use NeoPixel (WS2812) individually addressable RGB and 
RGBW LED strips with the micro:bit.
Warning
Do not use the 3v connector on the Microbit to power any more than 8 Neopixels at a 
time. If you wish to use more than 8 Neopixels, you must use a separate 3v-5v power 
supply for the Neopixel power pin. 
For an in depth explanation visit: 
https://microbit-micropython.readthedocs.io/en/v2-docs/neopixel.html"""

#Classes

class NeoPixel(pin, n, bpp=3):
    """ Initialise a new strip of n number of neopixel LEDs controlled via pin pin. 
    To support RGBW neopixels, a third argument can be passed to NeoPixel to 
    indicate the number of bytes per pixel (bpp). For RGBW, this is is 4 rather 
    than the default of 3 for RGB and GRB.

    Each pixel is addressed by a position (starting from 0). Neopixels are given 
    RGB (red, green, blue) / RGBW (red, green, blue, white) values between 0-255 
    as a tuple. For example, in RGB, (255,255,255) is white. In RGBW, 
    (255,255,255,0) or (0,0,0,255) is white. """

    def clear():
        """ Clear all the pixels. """
        pass

    def show():
        """ Show the pixels. Must be called for any updates to become visible. """
        pass

    def write():
        """ For micro:bit V2, an additional write() method is available and is 
        equivalent to show() """
        pass

    def fill(colour):
        """ V2 Colour all pixels a given RGB/RGBW value. The colour argument should be 
        a tuple of the same length as the number of bytes per pixel (bpp). For example 
        fill((0,0,255)). Use in conjunction with show() to update the Neopixels. """
        pass

