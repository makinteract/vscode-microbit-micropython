#Accelerometer

""" This module gives you access to the on-board accelerometer.
By default MicroPython sets the accelerometer range to +/- 2000 mg (g being a unit of 
acceleration based on the standard gravity), which configures the maximum and minimum 
values returned by the accelerometer functions. The range can be changed via set_range().

The accelerometer also provides convenience functions for detecting gestures. The 
recognised gestures are represented as strings: up, down, left, right, face up, face down, 
freefall, 3g, 6g, 8g, shake.

Note:
Gestures are not updated in the background so there needs to be constant calls to some 
accelerometer method to do the gesture detection. Usually gestures can be detected using a 
loop with a small sleep() delay.
Functions """

#Functions

def get_x():
    """ Returns:	The acceleration measurement in the x axis in milli-g, as a positive or 
    negative integer. """
    pass

def get_y():
    """ Returns:	The acceleration measurement in the y axis in milli-g, as a positive or 
    negative integer. """
    pass

def get_z():
    """ Returns:	The acceleration measurement in the z axis in milli-g, as a positive or 
    negative integer. """
    pass

def get_values():
    """ Returns:	The acceleration measurements in all axes at once, as a three-element tuple 
    of integers ordered as X, Y, Z. """
    pass

def get_strength():
    """ Get the acceleration measurement of all axes combined, as a positive integer. This is the 
    Pythagorean sum of the X, Y and Z axes.
    Returns:	The combined acceleration strength of all the axes, in milli-g. """
    pass

def current_gesture():
    """ Returns:	String with the name of the current gesture. """
    pass

def is_gesture(name):
    """ Parameters:	name – String with the name of the gesture to check.
    Returns:	Boolean indicating if the named gesture is currently active. """
    pass

def was_gesture(name):
    """ Parameters:	name – String with the name of the gesture to check.
    Returns:	Boolean indicating if the named gesture was active since the last call. """
    pass

def get_gestures():
    """ Get a historical list of the registered gestures.
    Calling this function clears the gesture history before returning.
    Returns:	A tuple of the gesture history, most recent is listed last. """
    pass

def set_range(value):
    """ Set the accelerometer sensitivity range, in g (standard gravity), to the closest values 
    supported by the hardware, so it rounds to either 2, 4, or 8 g.
    Parameters:	value – New range for the accelerometer, an integer in g. """
    pass