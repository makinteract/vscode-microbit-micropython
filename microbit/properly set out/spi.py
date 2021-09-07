from __init__ import *

def init(baudrate=1000000, bits=8, mode=0, sclk=pin13, mosi=pin15, miso=pin14):
    """see: https://microbit-micropython.readthedocs.io/en/latest/spi.html"""

def read(nbytes):
    """Read at most nbytes. Returns what was read."""

def write(buffer):
    """Write the buffer of bytes to the bus."""

def write_readinto(out, inBuffer):
    """Write the out buffer to the bus and read any response into the in buffer. The length of the buffers should be the same. The buffers can be the same object."""