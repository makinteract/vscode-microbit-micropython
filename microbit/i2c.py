from microbit import pin19, pin20
#I²C

""" The i2c module lets you communicate with devices connected to your board using the I²C bus 
protocol. There can be multiple slave devices connected at the same time, and each one has 
its own unique address, that is either fixed for the device or configured on it. Your board 
acts as the I²C master. """

#Functions

def init(freq=100000, sda=pin20, scl=pin19):
    """  Re-initialize peripheral with the specified clock frequency freq on the specified sda 
    and scl pins.

    Warning
    On a micro:bit V1 board, changing the I²C pins from defaults will make the accelerometer 
    and compass stop working, as they are connected internally to those pins. This warning 
    does not apply to the V2 revision of the micro:bit as this has separate I²C lines for the 
    motion sensors and the edge connector. """
    pass

def scan():
    """ Scan the bus for devices. Returns a list of 7-bit addresses corresponding to those 
    devices that responded to the scan. """
    pass

def read(addr, n, repeat=False):
    """ Read n bytes from the device with 7-bit address addr. If repeat is True, no stop bit 
    will be sent. """
    pass

def write(addr, buf, repeat=False):
    """ Write bytes from buf to the device with 7-bit address addr. If repeat is True, no stop 
    bit will be sent. """
    pass