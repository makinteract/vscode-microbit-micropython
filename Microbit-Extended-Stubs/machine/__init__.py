#Machine

""" The machine module contains specific functions related to the micro:bit 
hardware. Most functions in this module allow to achieve direct and 
unrestricted access to and control of hardware blocks on a system 
(like CPU, timers, buses, etc.). Used incorrectly, this can lead to 
malfunction, lockups, crashes of your board, and in extreme cases, 
hardware damage. """

#Functions

def unique_id():
    """ Returns a byte string with a unique identifier of a board. It will 
    vary from one board instance to another. """
    pass

def reset():
    """ Resets the device in a manner similar to pushing the 
    external RESET button. """
    pass

def freq():
    """ Returns CPU frequency in hertz. """
    pass

def disable_irq():
    """ Disable interrupt requests. Returns the previous IRQ state which 
    should be considered an opaque value. This return value should 
    be passed to the machine.enable_irq() function to restore interrupts 
    to their original state, before machine.disable_irq() was called. """
    pass

def enable_irq(state):
    """ Re-enable interrupt requests. The state parameter should be the value 
    that was returned from the most recent call to the machine.disable_irq() 
    function. """
    pass

def time_pulse_us(pin, pulse_level, timeout_us=1000000):
    """ Time a pulse on the given pin, and return the duration of the pulse 
    in microseconds. The pulse_level argument should be 0 to time a low 
    pulse or 1 to time a high pulse.

    If the current input value of the pin is different to pulse_level, 
    the function first (*) waits until the pin input becomes equal to 
    pulse_level, then (**) times the duration that the pin is equal to 
    pulse_level. If the pin is already equal to pulse_level then timing 
    starts straight away.

    The function will return -2 if there was timeout waiting for condition 
    marked (*) above, and -1 if there was timeout during the main measurement, 
    marked (**) above. The timeout is the same for both cases and given by 
    timeout_us (which is in microseconds). """
    pass

Reading Memory

The machine module allows you to read from the device’s memory, 
getting 1 byte (8 bits; mem8), 2 byte (16 bits; mem16), or 4 byte 
(32 bits; mem32) words from physical addresses. For example: mem8[0x00] 
reads 1 byte on physical address 0x00. This has a number of uses, for 
example if you’d like to read data from the nRF51 registers.
