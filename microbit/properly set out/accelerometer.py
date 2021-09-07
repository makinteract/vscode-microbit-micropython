def get_x():
    """Get the acceleration measurement in the x axis, as a positive or negative integer, depending on the direction. The measurement is given in milli-g. By default the accelerometer is configured with a range of +/- 2g, and so this method will return within the range of +/- 2000mg."""
    return 2

def get_y():
    """Get the acceleration measurement in the y axis, as a positive or negative integer, depending on the direction. The measurement is given in milli-g. By default the accelerometer is configured with a range of +/- 2g, and so this method will return within the range of +/- 2000mg."""
    return 2

def get_z():
    """Get the acceleration measurement in the z axis, as a positive or negative integer, depending on the direction. The measurement is given in milli-g. By default the accelerometer is configured with a range of +/- 2g, and so this method will return within the range of +/- 2000mg."""
    return 2

def get_values():
    """Get the acceleration measurements in all axes at once, as a three-element tuple of integers ordered as X, Y, Z. By default the accelerometer is configured with a range of +/- 2g, and so X, Y, and Z will be within the range of +/-2000mg."""
    return (2,2,2)

def current_gesture():
    """Return the name of the current gesture."""
    return "face up"

def is_gesture(name):
    """Return True or False to indicate if the named gesture is currently active."""
    return False

def was_gesture(name):
    """Return True or False to indicate if the named gesture was active since the last call."""
    return False

def get_gestures():
    """Return a tuple of the gesture history. The most recent is listed last. Also clears the gesture history before returning."""
    return ()