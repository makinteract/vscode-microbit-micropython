def get_pixel(x,y):
    """get the brightness of the addressed pixel"""
    return 9

def set_pixel(x,y,value):
    """set the brightness of the addressed pixel"""
    z = value

def clear():
    """clears the display"""
    z = 0

def show(*args):
    """shows the image. Use either:
    show(image)
    shows the image on the display.
    or
    show(value, <>delay, <>*, <>wait, <>loop, <>clear), where fields marked with <> are optional
    If value is a string, float or integer, display letters/digits in sequence. Otherwise, if value is an iterable sequence of images, display these images in sequence. Each letter, digit or image is shown with delay milliseconds between them.
If wait is True, this function will block until the animation is finished, otherwise the animation will happen in the background.
If loop is True, the animation will repeat forever.
If clear is True, the display will be cleared after the iterable has finished.
Note that the wait, loop and clear arguments must be specified using their keyword."""
    z = 0

def scroll(value, delay=150, *, wait=True, loop=False, monospace=False):
    """Scrolls value horizontally on the display. If value is an integer or float it is first converted to a string using str(). The delay parameter controls how fast the text is scrolling.
If wait is True, this function will block until the animation is finished, otherwise the animation will happen in the background.
If loop is True, the animation will repeat forever.
If monospace is True, the characters will all take up 5 pixel-columns in width, otherwise there will be exactly 1 blank pixel-column between each character as they scroll.
Note that the wait, loop and monospace arguments must be specified using their keyword."""
    z = 0

def on():
    """turn on the display"""
    z = 0

def off():
    """turn off the display"""
    z = 0

def is_on():
    """returns true if the display is on"""
    return True

def read_light_level():
    """Use the display’s LEDs in reverse-bias mode to sense the amount of light falling on the display. Returns an integer between 0 and 255 representing the light level, with larger meaning more light."""
    return 255
