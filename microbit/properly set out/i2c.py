from __init__ import *

def init(freq=100000, sda=pin20, scl=pin19):
    """Re-initialize peripheral with the specified clock frequency freq on the specified sda and scl pins.
Warning
Changing the I²C pins from defaults will make the accelerometer and compass stop working, as they are connected internally to those pins."""

def scan():
    """Scan the bus for devices. Returns a list of 7-bit addresses corresponding to those devices that responded to the scan."""
    return []

def read(addr, n, repeat=False):
    """Read n bytes from the device with 7-bit address addr. If repeat is True, no stop bit will be sent."""

def write(addr, buf, repeat=False):
    """Write bytes from buf to the device with 7-bit address addr. If repeat is True, no stop bit will be sent."""
