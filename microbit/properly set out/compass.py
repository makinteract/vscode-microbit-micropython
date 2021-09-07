def calibrate():
    """Starts the calibration process. An instructive message will be scrolled to the user after which they will need to rotate the device in order to draw a circle on the LED display."""

def is_calibrated():
    """Returns True if the compass has been successfully calibrated, and returns False otherwise."""
    return True

def clear_calibration():
    """Undoes the calibration, making the compass uncalibrated again."""

def get_x():
    """Gives the reading of the magnetic field strength on the x axis in nano tesla, as a positive or negative integer, depending on the direction of the field."""
    return 0

def get_y():
    """Gives the reading of the magnetic field strength on the y axis in nano tesla, as a positive or negative integer, depending on the direction of the field."""
    return 0

def get_z():
    """Gives the reading of the magnetic field strength on the z axis in nano tesla, as a positive or negative integer, depending on the direction of the field."""
    return 0

def heading():
    """Gives the compass heading, calculated from the above readings, as an integer in the range from 0 to 360, representing the angle in degrees, clockwise, with north as 0."""
    return 0

def get_field_strength():
    """Returns an integer indication of the magnitude of the magnetic field around the device in nano tesla."""
    return 0