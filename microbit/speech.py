# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from microbit import (
    _MicroBitAnalogDigitalPin,
    pin0,
)


def translate(words: str) -> str:
    """
    Return a string containing the phonemes for the English words in the
    string 'words'.
    """
    pass


def say(
    words: str,
    pitch: int = 64,
    speed: int = 72,
    mouth: int = 128,
    throat: int = 128,
) -> None:
    """
    Say the English words in the string 'words'.
    Override the optional pitch, speed, mouth and throat settings to change
    the tone of voice.
    """
    pass


def pronounce(
    phonemes: str,
    pitch: int = 64,
    speed: int = 72,
    mouth: int = 128,
    throat: int = 128,
) -> None:
    """
    Pronounce the phonemes in the string 'phonemes'.
    Override the optional pitch, speed, mouth and throat settings to change
    the tone of voice.
    """
    pass


def sing(
    song: str,
    pitch: int = 64,
    speed: int = 72,
    mouth: int = 128,
    throat: int = 128,
) -> None:
    """
    Sing the phonemes in the string 'song'.
    Add pitch information to a phoneme with a hash followed by a number
    between 1-255 like this: '#112DOWWWWWWWW'.
    Override the optional pitch, speed, mouth and throat settings to change
    the tone of voice.
    """
    pass


# V2

def say(
    words: str,
    pitch: int = 64,
    speed: int = 72,
    mouth: int = 128,
    throat: int = 128,
    pin: _MicroBitAnalogDigitalPin = pin0,
) -> None:
    """
    Say the English words in the string 'words'.
    Override the optional pitch, speed, mouth and throat settings to change 
    the tone of voice.
    For micro:bit V2 an optional argument to specify the output pin can be 
    used to override the default of pin0. If we do not want any sound to 
    play out of the pins can use pin=None.
    """
    pass


def pronounce(
    phonemes: str,
    pitch: int = 64,
    speed: int = 72,
    mouth: int = 128,
    throat: int = 128,
    pin: _MicroBitAnalogDigitalPin = pin0,
) -> None:
    """
    Pronounce the phonemes in the string 'phonemes'.
    Override the optional pitch, speed, mouth and throat settings to change
    the tone of voice.
    For micro:bit V2 an optional argument to specify the output pin can be 
    used to override the default of pin0. If we do not want any sound to 
    play out of the pins can use pin=None.
    """
    pass


def sing(
    song: str,
    pitch: int = 64,
    speed: int = 72,
    mouth: int = 128,
    throat: int = 128,
    pin: _MicroBitAnalogDigitalPin = pin0,
) -> None:
    """
    Sing the phonemes in the string 'song'.
    Add pitch information to a phoneme with a hash followed by a number
    between 1-255 like this: '#112DOWWWWWWWW'.
    Override the optional pitch, speed, mouth and throat settings to change
    the tone of voice.
    For micro:bit V2 an optional argument to specify the output pin can be 
    used to override the default of pin0. If we do not want any sound to 
    play out of the pins can use pin=None.
    """
    pass