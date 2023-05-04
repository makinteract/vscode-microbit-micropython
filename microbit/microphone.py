#Microphone V2

""" This object lets you access the built-in microphone available on the micro:bit V2. It can 
be used to respond to sound. The microphone input is located on the front of the board 
alongside a microphone activity LED, which is lit when the microphone is in use. """


#Sound events

""" The microphone can respond to a pre-defined set of sound events that are based on the 
amplitude and wavelength of the sound. These sound events are represented by instances of 
the SoundEvent class, accessible via variables in SoundEvent:
    SoundEvent.QUIET: Represents the transition of sound events, from loud to quiet 
    like speaking or background music.
    SoundEvent.LOUD: Represents the transition of sound events, from quiet to loud 
    like clapping or shouting. """

#Functions
    
def current_event():
    """ return: the name of the last recorded sound event, SoundEvent('loud') or 
    SoundEvent('quiet'). """
    pass

def was_event(event):
    """ event: a sound event, such as SoundEvent.LOUD or SoundEvent.QUIET.
    return: true if sound was heard at least once since the last call, 
    otherwise false. was_event() also clears the sound event history before returning. """
    pass

def is_event(event):
    """ event: a sound event, such as SoundEvent.LOUD or SoundEvent.QUIET.
    return: true if sound event is the most recent since the last call, otherwise false. 
    It does not clear the sound event history. """
    pass

def get_events():
    """ return: a tuple of the event history. The most recent is listed last. get_events() 
    also clears the sound event history before returning. """
    pass

def set_threshold(event, value):
    """ event: a sound event, such as SoundEvent.LOUD or SoundEvent.QUIET.
    value: The threshold level in the range 0-255. For example, 
    set_threshold(SoundEvent.LOUD, 250) will only trigger if the sound is very 
    loud (>= 250). """
    pass

def sound_level():
    """ return: a representation of the sound pressure level in the range 0 to 255. """
    pass