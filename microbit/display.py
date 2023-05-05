#Display
""" This module controls the 5×5 LED display on the front of your board. It can be used to 
display images, animations and even text. """

#Functions

def get_pixel(x, y):
    """ Return the brightness of the LED at column x and row y as an integer between 0 (off) 
    and 9 (bright). """
    pass

def set_pixel(x, y, value):
    """ Set the brightness of the LED at column x and row y to value, which has to be an integer 
    between 0 and 9. """
    pass

def clear():
    """ Set the brightness of all LEDs to 0 (off). """
    pass

def show(image, delay=400, *, wait=True, loop=False, clear=False):
    """ If image is a string, float or integer, display letters/digits in sequence. Otherwise, 
    if image is an iterable sequence of images, display these images in sequence. Each letter,
    digit or image is shown with delay milliseconds between them.

    If wait is True, this function will block until the animation is finished, otherwise the 
    animation will happen in the background.

    If loop is True, the animation will repeat forever.

    If clear is True, the display will be cleared after the iterable has finished.

    Note that the wait, loop and clear arguments must be specified using their keyword. """
    pass

def scroll(text, delay=150, *, wait=True, loop=False, monospace=False):
    """ Scrolls text horizontally on the display. If text is an integer or float it is first 
    converted to a string using str(). The delay parameter controls how fast the text is 
    scrolling.

    If wait is True, this function will block until the animation is finished, otherwise the 
    animation will happen in the background.

    If loop is True, the animation will repeat forever.

    If monospace is True, the characters will all take up 5 pixel-columns in width, otherwise 
    there will be exactly 1 blank pixel-column between each character as they scroll.

    Note that the wait, loop and monospace arguments must be specified using their keyword. """
    pass

def on():
    """ Use on() to turn on the display. """
    pass

def off():
    """ Use off() to turn off the display (thus allowing you to re-use the GPIO pins associated 
    with the display for other purposes). """
    pass

def is_on():
    """ Returns True if the display is on, otherwise returns False. """
    pass

def read_light_level():
    """ Use the display’s LEDs in reverse-bias mode to sense the amount of light falling on 
    the display. Returns an integer between 0 and 255 representing the light level, with 
    larger meaning more light. """
    pass
