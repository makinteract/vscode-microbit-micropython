"""Micro:Bit stubs for Visual Studio Code

Joseph Fergusson, 2019"""

class _display:
    def get_pixel(self,x,y):
        """get the brightness of the addressed pixel"""
        return 9

    def set_pixel(self,x,y,value):
        """set the brightness of the addressed pixel"""
        z = value

    def clear(self):
        """clears the display"""
        z = 0

    def show(self,*args):
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

    def scroll(self,value, delay=150, *, wait=True, loop=False, monospace=False):
        """Scrolls value horizontally on the display. If value is an integer or float it is first converted to a string using str(). The delay parameter controls how fast the text is scrolling.
    If wait is True, this function will block until the animation is finished, otherwise the animation will happen in the background.
    If loop is True, the animation will repeat forever.
    If monospace is True, the characters will all take up 5 pixel-columns in width, otherwise there will be exactly 1 blank pixel-column between each character as they scroll.
    Note that the wait, loop and monospace arguments must be specified using their keyword."""
        z = 0

    def on(self):
        """turn on the display"""
        z = 0

    def off(self):
        """turn off the display"""
        z = 0

    def is_on(self):
        """returns true if the display is on"""
        return True

    def read_light_level(self):
        """Use the display’s LEDs in reverse-bias mode to sense the amount of light falling on the display. Returns an integer between 0 and 255 representing the light level, with larger meaning more light."""
        return 255

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

button_a = _Button()
button_b = _Button()

pin_logo = _MicroBitTouchPin()

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

display = _display()

class _Image:
        """Base image class"""

        def width(self):
            """gets the number of columns in an image"""
            return 5

        def height(self):
            """gets the number of rows in an image"""
            return 5

        def set_pixel(self,x,y,value):
            """sets the brightness of a pixel at the given position
            Cannot be used on inbuilt images."""
            a = 0

        def get_pixel(self,x,y):
            """returns the brightness of the pixel located at x,y"""
            return 9

        def shift_left(self,n):
            """returns a new image created by shifting the image left by n columns"""
            return self

        def shift_right(self,n):
            """returns a new image created by shifting the image right by n columns"""
            return self

        def shift_up(self,n):
            """returns a new image created by shifting the image up by n rows"""
            return self

        def shift_down(self,n):
            """returns a new image created by shifting the image down by n rows"""
            return self

        def crop(self,x,y,w,h):
            """return a new image by cropping the picture to a width of w and a height of h, starting with the pixel at column x and row y."""
            return self

        def copy(self):
            """return an exact copy of the image"""
            return self

        def invert(self):
            """return a new image by inverting the brightness of the pixels in the source image."""
            return self

        def fill(self,value):
            """Return a new image by inverting the brightness of the pixels in the source image.
            Cannot be used on inbuilt images."""
            return self

        def blit(self,src, x, y, w, h, xdest=0, ydest=0):
            """Copy the rectangle defined by x, y, w, h from the image src into this image at xdest, ydest. Areas in the source rectangle, but outside the source image are treated as having a value of 0."""
            a = 0

class _img(_Image):

    HEART = _Image()
    HEART_SMALL = _Image()

    HAPPY = _Image()
    SMILE = _Image()
    SAD = _Image()
    CONFUSED = _Image()
    ANGRY = _Image()
    ASLEEP = _Image()
    SURPRISED = _Image()
    SILLY = _Image()
    FABULOUS = _Image()
    MEH = _Image()

    YES = _Image()
    NO = _Image()

    CLOCK12 = _Image()
    CLOCK11 = _Image()
    CLOCK10 = _Image()
    CLOCK9 = _Image()
    CLOCK8 = _Image()
    CLOCK7 = _Image()
    CLOCK6 = _Image()
    CLOCK5 = _Image()
    CLOCK4 = _Image()
    CLOCK3 = _Image()
    CLOCK2 = _Image()
    CLOCK1 = _Image()

    ARROW_N = _Image()
    ARROW_NE = _Image()
    ARROW_E = _Image()
    ARROW_SE = _Image()
    ARROW_S = _Image()
    ARROW_SW = _Image()
    ARROW_W = _Image()
    ARROW_NW = _Image()

    TRIANGLE = _Image()
    TRIANGLE_LEFT = _Image()
    CHESSBOARD = _Image()
    DIAMOND = _Image()
    DIAMOND_SMALL = _Image()
    SQUARE = _Image()
    SQUARE_SMALL = _Image()

    RABBIT = _Image()
    COW = _Image()

    MUSIC_CROTCHET = _Image()
    MUSIC_QUAVER = _Image()
    MUSIC_QUAVERS = _Image()

    PITCHFORK = _Image()

    XMAS = _Image()

    PACMAN = _Image()
    TARGET = _Image()
    TSHIRT = _Image()
    ROLLERSKATE = _Image()
    DUCK = _Image()
    HOUSE = _Image()
    TORTOISE = _Image()
    BUTTERFLY = _Image()
    STICKFIGURE = _Image()
    GHOST = _Image()
    SWORD = _Image()
    GIRAFFE = _Image()
    SKULL = _Image()
    UMBRELLA = _Image()
    SNAKE = _Image()

    def __new__(self):
        return self


Image = _img()
#def Image(string = None, width=None, height=None, buffer=None, fake=None):
#    if (fake == True):
#        return _img
#    else:
#        return _img._Image

class _spi:
    def init(self,baudrate=1000000, bits=8, mode=0, sclk=pin13, mosi=pin15, miso=pin14):
        """see: https://microbit-micropython.readthedocs.io/en/latest/spi.html"""

    def read(self,nbytes):
        """Read at most nbytes. Returns what was read."""

    def write(self,buffer):
        """Write the buffer of bytes to the bus."""

    def write_readinto(self,out, inBuffer):
        """Write the out buffer to the bus and read any response into the in buffer. The length of the buffers should be the same. The buffers can be the same object."""

spi = _spi()

class _uart:
    def init(self, baudrate=9600, bits=8, parity=None, stop=1, *, tx=None, rx=None):
        """Initialize serial communication with the specified parameters on the specified tx and rx pins. Note that for correct communication, the parameters have to be the same on both communicating devices."""

    def any(self):
        """Return True if any data is waiting, else False."""
        return True

    def read(self,nBytes = None):
        """Read at most n Bytes if the parameter is set, else read as much as can be read.
        Returns a Byte array if data can be read, otherwise returns None."""
        return None

    def readInto(self,buf, nBytes = None):
        """Read bytes into the buf. If nbytes is specified then read at most that many bytes. Otherwise, read at most len(buf) bytes.
    Return value: number of bytes read and stored into buf or None on timeout."""
        
    def readline(self):
        """Read a line, ending in a newline character.
    Return value: the line read or None on timeout. The newline character is included in the returned bytes."""

    def write(self,buf):
        """Write the buffer to the bus, it can be a bytes object or a string.
        Return value: number of bytes written or None on timeout."""

uart = _uart()

class _i2c:
    def init(self,freq=100000, sda=pin20, scl=pin19):
        """Re-initialize peripheral with the specified clock frequency freq on the specified sda and scl pins.
    Warning
    Changing the I²C pins from defaults will make the accelerometer and compass stop working, as they are connected internally to those pins."""

    def scan(self):
        """Scan the bus for devices. Returns a list of 7-bit addresses corresponding to those devices that responded to the scan."""
        return []

    def read(self,addr, n, repeat=False):
        """Read n bytes from the device with 7-bit address addr. If repeat is True, no stop bit will be sent."""

    def write(self,addr, buf, repeat=False):
        """Write bytes from buf to the device with 7-bit address addr. If repeat is True, no stop bit will be sent."""

i2c = _i2c()

class _compass:
    def calibrate(self):
        """Starts the calibration process. An instructive message will be scrolled to the user after which they will need to rotate the device in order to draw a circle on the LED display."""

    def is_calibrated(self):
        """Returns True if the compass has been successfully calibrated, and returns False otherwise."""
        return True

    def clear_calibration(self):
        """Undoes the calibration, making the compass uncalibrated again."""

    def get_x(self):
        """Gives the reading of the magnetic field strength on the x axis in nano tesla, as a positive or negative integer, depending on the direction of the field."""
        return 0

    def get_y(self):
        """Gives the reading of the magnetic field strength on the y axis in nano tesla, as a positive or negative integer, depending on the direction of the field."""
        return 0

    def get_z(self):
        """Gives the reading of the magnetic field strength on the z axis in nano tesla, as a positive or negative integer, depending on the direction of the field."""
        return 0

    def heading(self):
        """Gives the compass heading, calculated from the above readings, as an integer in the range from 0 to 360, representing the angle in degrees, clockwise, with north as 0."""
        return 0

    def get_field_strength(self):
        """Returns an integer indication of the magnitude of the magnetic field around the device in nano tesla."""
        return 0

compass = _compass()

class _accelerometer:
    def get_x(self):
        """Get the acceleration measurement in the x axis, as a positive or negative integer, depending on the direction. The measurement is given in milli-g. By default the accelerometer is configured with a range of +/- 2g, and so this method will return within the range of +/- 2000mg."""
        return 2

    def get_y(self):
        """Get the acceleration measurement in the y axis, as a positive or negative integer, depending on the direction. The measurement is given in milli-g. By default the accelerometer is configured with a range of +/- 2g, and so this method will return within the range of +/- 2000mg."""
        return 2

    def get_z(self):
        """Get the acceleration measurement in the z axis, as a positive or negative integer, depending on the direction. The measurement is given in milli-g. By default the accelerometer is configured with a range of +/- 2g, and so this method will return within the range of +/- 2000mg."""
        return 2

    def get_values(self):
        """Get the acceleration measurements in all axes at once, as a three-element tuple of integers ordered as X, Y, Z. By default the accelerometer is configured with a range of +/- 2g, and so X, Y, and Z will be within the range of +/-2000mg."""
        return (2,2,2)

    def current_gesture(self):
        """Return the name of the current gesture."""
        return "face up"

    def is_gesture(self,name):
        """Return True or False to indicate if the named gesture is currently active."""
        return False

    def was_gesture(self,name):
        """Return True or False to indicate if the named gesture was active since the last call."""
        return False

    def get_gestures(self):
        """Return a tuple of the gesture history. The most recent is listed last. Also clears the gesture history before returning."""
        return ()

accelerometer = _accelerometer()


"""Image stuff"""
#def Image(string = None, width=None, height=None, buffer=None):
#"""Image() - Create a blank 5x5 image
#Image(string) - Create an image by parsing the string, a single character returns that glyph
#Image(width, height) - Create a blank image of given size
#Image(width, height, buffer) - Create an image from the given buffer"""
#    return Image._Image()
