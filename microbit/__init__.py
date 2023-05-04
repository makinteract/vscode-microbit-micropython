import accelerometer
import audio
import compass
import display
import i2c
import microphone
import neopixel
import radio
import speaker
import speech
import spi
import uart

#Functions

def panic():
    """ Enter a panic mode that stops all execution, scrolls an 
    error code in the micro:bit display and requires restart.
    Parameters:	n – An arbitrary integer between 0 and 255 
    to indicate an error code. """
    pass

def reset():
    """ Restart the board. """
    pass

def running_time():
    """ Returns:	The number of milliseconds since the board was switched on or restarted. """
    pass

def scale(value, from_, to):
    """ Converts a value from a range to another range.
    For example, to convert 30 degrees from Celsius to Fahrenheit:
    temp_fahrenheit = scale(30, from_=(0.0, 100.0), to=(32.0, 212.0))

    This can be useful to convert values between inputs and outputs, 
    for example an accelerometer x value to a speaker volume.

    If one of the numbers in the to parameter is a floating point 
    (i.e a decimal number like 10.0), this function will return a floating point 
    number. If they are both integers (i.e 10), it will return an integer:

    returns_int = scale(accelerometer.get_x(), from_=(-2000, 2000), to=(0, 255))

    Negative scaling is also supported, for example scale(25, from_=(0, 100), 
    to=(0, -200)) will return -50.

    Parameters:	
        value – A number to convert.
        from – A tuple to define the range to convert from.
        to – A tuple to define the range to convert to.

    Returns:
        The value converted to the to range. """
    pass

def set_volume(volume):
    """ (V2 only) Configure the output volume of the micro:bit speaker and pins.
    Parameters:	volume – An integer between 0 and 255 to set the volume. """
    pass

def sleep(n):
    """ Wait for n milliseconds. One second is 1000 milliseconds.
    Parameters:	n – An integer or floating point number indicating the number 
    of milliseconds to wait. """
    pass

def run_every(callback, days=None, h=None, min=None, s=None, ms=None):
    """ Schedule to run a function at the interval specified by the time arguments.
    run_every can be used in two ways:
        As a Decorator - placed on top of the function to schedule. For example:

        @run_every(days=1, h=1, min=20, s=30, ms=50)
        def my_function():
            # Do something here

        As a Function - passing the callback as a positional argument. For example:

        def my_function():
            # Do something here
        run_every(my_function, s=30)

    Each argument corresponds to a different time unit and they are additive. 
    So run_every(min=1, s=30) schedules the callback every minute and a half.

    When an exception is thrown inside the callback function it deschedules the function. 
    To avoid this you can catch exceptions with try/except.
    Parameters:	

        callback – Function to call at the provided interval.
        days – Sets the days mark for the scheduling.
        h – Sets the hour mark for the scheduling.
        min – Sets the minute mark for the scheduling.
        s – Sets the second mark for the scheduling.
        ms – Sets the millisecond mark for the scheduling. """
    pass

def temperature():
    """ Returns:	An integer with the temperature of the micro:bit in degrees Celcius. """
    pass

#Attributes-Buttons

class _Button():
    """ Represents a button.
    Note: This class is not actually available to the user, it is only used by the 
    two button instances, which are provided already initialized. """
    def __init__(self) -> None:
        pass

    def is_pressed():
        """ Returns True if the specified button button is currently being held down, 
        and False otherwise. """
        pass

    def was_pressed():
        """ Returns True or False to indicate if the button was pressed (went from up to down) 
        since the device started or the last time this method was called. Calling this 
        method will clear the press state so that the button must be pressed again before 
        this method will return True again. """
        pass

    def get_presses():
        """ Returns the running total of button presses, and resets this total 
        to zero before returning. """
        pass

button_a = _Button()
""" A Button instance representing the left button. """

button_b = _Button()
""" Represents the right button. """

#Attributes-Input/Output Pins

""" There are three kinds of pins, differing in what is available for them. They 
are represented by the classes listed below. Note that they form a hierarchy, 
so that each class has all the functionality of the previous class, and adds 
its own to that.

Note:
Those classes are not actually available for the user, you can’t create new 
instances of them. You can only use the instances already provided, representing 
the physical pins on your board. """

class _MicroBitDigitalPin():

    def __init__(self) -> None:
        pass

    def read_digital():
        """ Return 1 if the pin is high, and 0 if it’s low. """
        pass

    def write_digital(value):
        """ Set the pin to high if value is 1, or to low, if it is 0. """
        pass

    def set_pull(value):
        """ Set the pull state to one of three possible values: pin.PULL_UP, pin.PULL_DOWN or 
        pin.NO_PULL (where pin is an instance of a pin).
        The pull mode for a pin is automatically configured when the pin changes to an input 
        mode. Input modes are when you call read_analog / read_digital / is_touched. The 
        default pull mode for these is, respectively, NO_PULL, PULL_DOWN, PULL_UP. Calling 
        set_pull will configure the pin to be in read_digital mode with the given pull mode. """
        pass

    def get_pull():
        """ Returns the pull configuration on a pin, which can be one of three possible values: 
        NO_PULL, PULL_DOWN, or PULL_UP. These are set using the set_pull() method or 
        automatically configured when a pin mode requires it. """
        pass

    def get_mode():
        """ Returns the pin mode. When a pin is used for a specific function, like writing a 
        digital value, or reading an analog value, the pin mode changes. Pins can have one of 
        the following modes: "unused", "analog", "read_digital", "write_digital", "display", 
        "button", "music", "audio", "touch", "i2c", "spi". """
        pass

    def write_analog(value):
        """ Output a PWM signal on the pin, with the duty cycle proportional to the provided 
        value. The value may be either an integer or a floating point number between 0 
        (0% duty cycle) and 1023 (100% duty). """
        pass

    def set_analog_period(period):
        """ Set the period of the PWM signal being output to period in milliseconds. The minimum 
        valid value is 1ms. """
        pass

    def set_analog_period_microseconds(period):
        """ Set the period of the PWM signal being output to period in microseconds. The minimum 
        valid value is 256µs. """
        pass

    def get_analog_period_microseconds():
        """ Returns the configured period of the PWM signal in microseconds. """
        pass

class _MicroBitAnalogDigitalPin(_MicroBitDigitalPin):
    
    def __init__(self) -> None:
        pass

    def read_analog():
        """ Read the voltage applied to the pin, and return it as an integer 
        between 0 (meaning 0V) and 1023 (meaning 3.3V). """
        pass
    
class _MicroBitTouchPin(_MicroBitAnalogDigitalPin):

    def __init__(self) -> None:
        pass

    def is_touched():
        """ Return True if the pin is being touched with a finger, otherwise return False.
        Note:
        The default touch mode for the pins on the edge connector is resistive. The default 
        for the logo pin V2 is capacitive.
        Resistive touch This test is done by measuring how much resistance there is between 
        the pin and ground. A low resistance gives a reading of True. To get a reliable 
        reading using a finger you may need to touch the ground pin with another part of your 
        body, for example your other hand.
        Capacitive touch This test is done by interacting with the electric field of a 
        capacitor using a finger as a conductor. Capacitive touch does not require you to make 
        a ground connection as part of a circuit. """
        pass

    def set_touch_mode(value):
        """ Set the touch mode for the given pin. Value can be either CAPACITIVE or RESISTIVE. 
        For example, pin0.set_touch_mode(pin0.CAPACITIVE). """
        pass
    
pin_logo = _MicroBitTouchPin()
""" A touch sensitive logo pin on the front of the micro:bit, which by default is set to 
capacitive touch mode. """
pin_speaker = _MicroBitAnalogDigitalPin()
""" A pin to address the micro:bit speaker. This API is intended only for use in Pulse-Width 
Modulation pin operations eg. pin_speaker.write_analog(128). """

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
pin12 = _MicroBitDigitalPin()
pin13 = _MicroBitDigitalPin()
pin14 = _MicroBitDigitalPin()
pin15 = _MicroBitDigitalPin()
pin16 = _MicroBitDigitalPin()
# Pin17 = 3v3
# Pin18 = 3v3
pin19 = _MicroBitDigitalPin()
pin20 = _MicroBitDigitalPin()
# pin21 = gnd
# pin22 = gnd

""" Note:
GPIO pins are also used for the display, as described in the table above. If you want to use 
these pins for another purpose, you may need to turn the display off. For more info see the 
edge connector data sheet. """

#Class-Image
""" The Image class is used to create images that can be displayed easily on the device’s LED 
matrix. Given an image object it’s possible to display it via the display API:
display.show(Image.HAPPY) """


class Image():
    """ There are four ways in which you can construct an image:
        Image() - Create a blank 5x5 image
        Image(string) 
            Create an image by parsing the string,
                image = Image("90009:"
                            "09090:"
                            "00900:"
                            "09090:"
                            "90009") 
            will create a 5×5 image of an X. The end of a line is indicated by a colon. It’s also 
            possible to use a newline (\n) to indicate the end of a line.
            A single character returns that glyph.
        Image(width, height)
            Creates an empty image with width columns and height rows. 
        Image(width, height, buffer)
            Optionally buffer can be an array of width``×``height integers in range 0-9 to 
            initialize the image:
            Image(2, 2, bytearray([9,9,9,9])) """
    def __init__(self) -> None:
        pass
    
    def width():
        """ Return the number of columns in the image. """
        pass

    def height():
        """ Return the numbers of rows in the image. """
        pass

    def set_pixel(x, y, value):
        """ Set the brightness of the pixel at column x and row y to the value, which has to be 
        between 0 (dark) and 9 (bright).
        This method will raise an exception when called on any of the built-in read-only 
        images, like Image.HEART. """
        pass

    def get_pixel(x, y):
        """ Return the brightness of pixel at column x and row y as an integer between 0 and 9. """
        pass

    def shift_left(n):
        """ Return a new image created by shifting the picture left by n columns. """
        pass

    def shift_right(n):
        """ Same as image.shift_left(-n). """
        pass

    def shift_up(n):
        """ Return a new image created by shifting the picture up by n rows. """
        pass
    def shift_down(n):
        """ Same as image.shift_up(-n). """
        pass

    def crop(x, y, w, h):
        """ Return a new image by cropping the picture to a width of w and a height of h, 
        starting with the pixel at column x and row y. """
        pass

    def copy():
        """ Return an exact copy of the image. """
        pass

    def invert():
        """ Return a new image by inverting the brightness of the pixels in the source image. """
        pass

    def fill(value):
        """ Set the brightness of all the pixels in the image to the value, which has to be 
        between 0 (dark) and 9 (bright).
        This method will raise an exception when called on any of the built-in read-only 
        images, like Image.HEART. """
        pass

    def blit(src, x, y, w, h, xdest=0, ydest=0):
        """ Copy the rectangle defined by x, y, w, h from the image src into this image at xdest, 
        ydest. Areas in the source rectangle, but outside the source image are treated as 
        having a value of 0.
        shift_left(), shift_right(), shift_up(), shift_down() and crop() can are all 
        implemented by using blit(). For example, img.crop(x, y, w, h) can be implemented as:

        def crop(self, x, y, w, h):
            res = Image(w, h)
            res.blit(self, x, y, w, h)
            return res """
        pass

    #Class-Image-Attributes
    """ The Image class also has the following built-in instances of itself included as its attributes
    (the attribute names indicate what the image represents): """

    HEART = None
    HEART_SMALL = None
    HAPPY = None
    SMILE = None
    SAD = None
    CONFUSED = None
    ANGRY = None
    ASLEEP = None
    SURPRISED = None
    SILLY = None
    FABULOUS = None
    MEH = None
    YES = None
    NO = None
    CLOCK12 = None
    CLOCK11 = None
    CLOCK10 = None
    CLOCK9 = None
    CLOCK8 = None
    CLOCK7 = None
    CLOCK6 = None
    CLOCK5 = None
    CLOCK4 = None
    CLOCK3 = None
    CLOCK2 = None
    CLOCK1 = None
    ARROW_N = None
    ARROW_NE = None
    ARROW_E = None
    ARROW_SE = None
    ARROW_S = None
    ARROW_SW = None
    ARROW_W = None
    ARROW_NW = None
    TRIANGLE = None
    TRIANGLE_LEFT = None
    CHESSBOARD = None
    DIAMOND = None
    DIAMOND_SMALL = None
    SQUARE = None
    SQUARE_SMALL = None
    RABBIT = None
    COW = None
    MUSIC_CROTCHET = None
    MUSIC_QUAVER = None
    MUSIC_QUAVERS = None
    PITCHFORK = None
    XMAS = None
    PACMAN = None
    TARGET = None
    TSHIRT = None
    ROLLERSKATE = None
    DUCK = None
    HOUSE = None
    TORTOISE = None
    BUTTERFLY = None
    STICKFIGURE = None
    GHOST = None
    SWORD = None
    GIRAFFE = None
    SKULL = None
    UMBRELLA = None
    SNAKE = None

    #Finally, related collections of images have been grouped together:

    ALL_CLOCKS = [None] #A list of all CLOCK images.
    ALL_ARROWS = [None] #A list of all ARROW images.

    #Class-Image-Attributes-Operations
    def repr(image_attribute):
        """ Get a compact string representation of the image attribute.
        Parameters: image_attribute - Name of image e.g. HEART"""
        pass

    def str(image_attribute):
        """ Get a readable string representation of the image. 
        Parameters: image_attribute - Name of image e.g. HEART """
        pass

    def addimg():
        """ Create a new image by adding the brightness values from the two images for each pixel. 
        Parameters: image_attribute - Name of image e.g. HEART """
        pass

    def multimg():
        """ Create a new image by multiplying the brightness of each pixel by n. 
        Parameters: image_attribute - Name of image e.g. HEART """
        pass

#Class-Sound

class Sound():
    """ Built-in sounds V2. The built-in sounds can be called using audio.play(Sound.NAME). """
    def __init__(self):
        pass

    GIGGLE = None
    HAPPY = None
    HELLO = None
    MYSTERIOUS = None
    SAD = None
    SLIDE = None
    SOARING = None
    SPRING = None
    TWINKLE = None
    YAWN = None

#Class-SoundEvent

class SoundEvent():
    """ The microphone can respond to a pre-defined set of sound events that are based on the 
    amplitude and wavelength of the sound. These sound events are represented by instances of 
    the SoundEvent class, accessible via variables in microbit.SoundEvent:

    microbit.SoundEvent.QUIET: Represents the transition of sound events, from loud to quiet 
                               like speaking or background music.
    microbit.SoundEvent.LOUD: Represents the transition of sound events, from quiet to loud 
                              like clapping or shouting.
    """
    def __init__(self):
        pass

    QUIET=None
    LOUD=None