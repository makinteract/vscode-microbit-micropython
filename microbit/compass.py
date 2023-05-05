#Compass
""" This module lets you access the built-in electronic compass. Before using, the compass should 
be calibrated, otherwise the readings may be wrong.

Warning:
Calibrating the compass will cause your program to pause until calibration is complete. 
Calibration consists of a little game to draw a circle on the LED display by rotating the 
device. """

#Functions

def calibrate():
    """ Starts the calibration process. An instructive message will be scrolled to the user after 
    which they will need to rotate the device in order to fill the LED display. """
    pass

def is_calibrated():
    """ Returns True if the compass has been successfully calibrated, and returns False otherwise. """
    pass

def clear_calibration():
    """ Undoes the calibration, making the compass uncalibrated again. """
    pass

def get_x():
    """ Gives the reading of the magnetic field strength on the x axis in nano tesla, as a 
    positive or negative integer, depending on the direction of the field. """
    pass

def get_y():
    """ Gives the reading of the magnetic field strength on the y axis in nano tesla, as a 
    positive or negative integer, depending on the direction of the field. """
    pass

def get_z():
    """ Gives the reading of the magnetic field strength on the z axis in nano tesla, as a 
    positive or negative integer, depending on the direction of the field. """
    pass

def heading():
    """ Gives the compass heading, calculated from the above readings, as an integer in the 
    range from 0 to 360, representing the angle in degrees, clockwise, with north as 0. """
    pass

def get_field_strength():
    """ Returns an integer indication of the magnitude of the magnetic field around the device 
    in nano tesla. """
    pass