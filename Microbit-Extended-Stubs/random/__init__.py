#Random Number Generation

""" This module is based upon the random module in the Python standard library. 
It contains functions for generating random behaviour. """

def getrandbits(n):
    """ Returns an integer with n random bits.

    Warning
    Because the underlying generator function returns at most 30 bits, 
    n may only be a value between 1-30 (inclusive). """
    pass

def seed(n):
    """ Initialize the random number generator with a known integer n. This 
    will give you reproducibly deterministic randomness from a given 
    starting state (n). """
    pass

def randint(a, b):
    """ Return a random integer N such that a <= N <= b. Alias for 
    randrange(a, b+1). """
    pass

def randrange(start, stop, step):
    """ Return a randomly selected element from range(start, stop, step).
    Parameters
    start 	Optional.   An integer specifying at which position to start. 
                        Default 0.
    stop 	Required.   An integer specifying at which position to end.
    step 	Optional.   An integer specifying the incrementation.
                        Default 1 """
    pass

def choice(seq):
    """ Return a random element from the non-empty sequence seq. If seq is 
    empty, raises IndexError. """
    pass

def random():
    """ Return the next random floating point number 
    in the range [0.0, 1.0) """
    pass

def uniform(a, b):
    """ Return a random floating point number N such that 
    a <= N <= b for a <= b and b <= N <= a for b < a. """
    pass
