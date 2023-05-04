#UART

""" The uart module lets you talk to a device connected to your board 
using a serial interface. 

Warning
    Initializing the UART on external pins will cause the Python console on USB to become 
    unaccessible, as it uses the same hardware. To bring the console back you must 
    reinitialize the UART without passing anything for tx or rx (or passing None to these 
    arguments). This means that calling uart.init(115200) is enough to restore the Python 
    console."""

#Functions

def init(baudrate=9600, bits=8, parity=None, stop=1, *, tx=None, rx=None):
    """ Initialize serial communication with the specified parameters on the specified 
    tx and rx pins. Note that for correct communication, the parameters have to be 
    the same on both communicating devices. """