#Speech

""" This module makes the micro:bit talk, sing and make other speech like sounds. By default 
sound output will be via the edge connector on pin 0 and the built-in speaker V2. You can 
connect wired headphones or a speaker to pin 0 and GND on the edge connector to hear the 
sound. For in depth explanation see: 
https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html """

#Functions

def translate(words):
    """ Given English words in the string words, return a string containing a best guess at 
    the appropriate phonemes to pronounce. The output is generated from this text to 
    phoneme translation table.
    This function should be used to generate a first approximation of phonemes that can be 
    further hand-edited to improve accuracy, inflection and emphasis. """
    pass

def pronounce(phonemes, *, pitch=64, speed=72, mouth=128, throat=128, pin=None):
    """ Pronounce the phonemes in the string phonemes. See below for details of how to use 
    phonemes to finely control the output of the speech synthesiser. Override the optional 
    pitch, speed, mouth and throat settings to change the timbre (quality) of the voice.
    For micro:bit V2 an optional argument to specify the output pin can be used to 
    override the default of pin0. If we do not want any sound to play out of the pins 
    can use pin=None. """
    pass

def say(words, *, pitch=64, speed=72, mouth=128, throat=128, pin=None):
    """ Say the English words in the string words. The result is semi-accurate for English. 
    Override the optional pitch, speed, mouth and throat settings to change the timbre 
    (quality) of the voice. This is a short-hand equivalent of: 
    speech.pronounce(speech.translate(words)) """
    pass

def sing(phonemes, *, pitch=64, speed=72, mouth=128, throat=128, pin=None):
    """ Sing the phonemes contained in the string phonemes. Changing the pitch and 
    duration of the note is described below. Override the optional pitch, speed, 
    mouth and throat settings to change the timbre (quality) of the voice. """
    pass