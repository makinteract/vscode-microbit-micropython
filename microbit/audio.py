from microbit import pin0
#Audio

""" This module allows you play sounds with the micro:bit.

By default sound output will be via the edge connector on pin 0 and the built-in speaker (V2).
You can connect wired headphones or a speaker to pin 0 and GND on the edge connector to hear 
the sounds. The audio module can be imported as import audio.

There are three different kinds of audio sources that can be played using 
the play() function:

    Built in sounds (V2), e.g. play(Sound.HAPPY)

    Sound Effects (V2), a way to create custom sounds by configuring its parameters:

    my_effect = audio.SoundEffect(freq_start=400, freq_end=2500, duration=500)
    audio.play(my_effect)

    Audio Frames, an iterable (like a list or a generator) of Audio Frames, which are lists 
    of 32 samples with values from 0 to 255:

    square_wave = AudioFrame()
    for i in range(16):
        square_wave[i] = 0
        square_wave[i + 16] = 255
    play([square_wave] * 64) """

#Functions

def play(source, wait=True, pin=pin0, return_pin=None):
    """ Play the audio source to completion.
    Parameters:	
        source – There are three types of data that can be used as a source:
            Sound:  The microbit module contains a list of built-in sounds, e.g. 
                    play(Sound.TWINKLE).
            SoundEffect: A sound effect, or an iterable of sound effects, created 
                        via the SoundEffect() class
            AudioFrame: An iterable of AudioFrame instances as described in the 
                        AudioFrame Technical Details section
        wait – If wait is True, this function will block until the source is exhausted.
        pin – An optional argument to specify the output pin can be used to override the 
                default of pin0. If we do not want any sound to play we can use pin=None.
        return_pin – specifies a differential edge connector pin to connect to an external 
                    speaker instead of ground. This is ignored for the V2 revision. """
    pass

def is_playing():
    """ Returns:	True if audio is playing, otherwise returns False. """
    pass

def stop():
    """ Stops all audio playback. """
    pass

#Sound Effects V2

WAVEFORM_SINE = None
WAVEFORM_SAWTOOTH=None
WAVEFORM_TRIANGLE=None
WAVEFORM_SQUARE=None
WAVEFORM_NOISE=None

FX_TREMOLO=None
FX_VIBRATO=None
FX_WARBLE=None
FX_NONE=None

SHAPE_LINEAR=None
SHAPE_CURVE=None
SHAPE_LOG=None

class SoundEffect(freq_start=500, freq_end=2500, duration=500, vol_start=255, vol_end=0, 
                  waveform=WAVEFORM_SQUARE, fx=FX_NONE, shape=SHAPE_LOG):

    """ An SoundEffect instance represents a sound effect, composed by a set of parameters 
    configured via the constructor or attributes.

    All the parameters are optional, with default values as shown above, and they can 
    all be modified via attributes of the same name. For example, we can first create an 
    effect my_effect = SoundEffect(duration=1000), and then change its attributes 
    my_effect.duration = 500.

    Parameters:	
        freq_start – Start frequency in Hertz (Hz), a number between 0 and 9999, default: 500
        freq_end – End frequency in Hertz (Hz), a number between 0 and 9999, default: 2500
        duration – Duration of the sound (ms), a number between 0 and 9999, default: 500
        vol_start – Start volume value, range 0-255, default: 255
        vol_end – End volume value, range 0-255, default: 0
        waveform – Type of waveform shape, one of these values: WAVEFORM_SINE, 
                   WAVEFORM_SAWTOOTH, WAVEFORM_TRIANGLE, WAVEFORM_SQUARE, 
                   WAVEFORM_NOISE (randomly generated noise). Default: WAVEFORM_SQUARE
        fx – Effect to add on the sound, one of the following values: FX_TREMOLO, FX_VIBRATO, 
             FX_WARBLE, or FX_NONE. Default: FX_NONE
        shape – The type of the interpolation curve between the start and end frequencies, 
                different wave shapes have different rates of change in frequency. One of the 
                following values: SHAPE_LINEAR, SHAPE_CURVE, SHAPE_LOG. Default: SHAPE_LOG """
    def __init__(self) -> None:
        pass

    def copy(self):
        """ Returns:	A copy of the SoundEffect. """
        pass

""" The arguments used to create any Sound Effect, can be inspected by looking at each of the 
SoundEffect instance attributes, or by converting the instance into a string (which can be 
done via str() function, or by using a function that does the conversion automatically like 
print()). """



#AudioFrame

class AudioFrame():
    """ An AudioFrame object is a list of 32 samples each of which is an unsigned byte 
    (whole number between 0 and 255). It takes just over 4 ms to play a single frame. """
    def __init__(self) -> None:
        pass

    def copyfrom(self, other):
        """ Overwrite the data in this AudioFrame with the data from another AudioFrame instance.
        Parameters:	other – AudioFrame instance from which to copy the data. """
        pass