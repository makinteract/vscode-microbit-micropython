def init(baudrate=9600, bits=8, parity=None, stop=1, *, tx=None, rx=None):
    """Initialize serial communication with the specified parameters on the specified tx and rx pins. Note that for correct communication, the parameters have to be the same on both communicating devices."""

def any():
    """Return True if any data is waiting, else False."""
    return True

def read(nBytes = None):
    """Read at most n Bytes if the parameter is set, else read as much as can be read.
    Returns a Byte array if data can be read, otherwise returns None."""
    return None

def readInto(buf, nBytes = None):
    """Read bytes into the buf. If nbytes is specified then read at most that many bytes. Otherwise, read at most len(buf) bytes.
Return value: number of bytes read and stored into buf or None on timeout."""
    
def readline():
    """Read a line, ending in a newline character.
Return value: the line read or None on timeout. The newline character is included in the returned bytes."""

def write(buf):
    """Write the buffer to the bus, it can be a bytes object or a string.
    Return value: number of bytes written or None on timeout."""