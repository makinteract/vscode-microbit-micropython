from __future__ import absolute_import, unicode_literals

from typing import Iterable, Tuple

from microbit import (
    _MicroBitAnalogDigitalPin,
    pin0,
    pin1,
)


class AudioFrame(list):
    """
    Represents a list of 32 samples each of which is a signed byte.
    It takes just over 4ms to play a single frame.
    """
    def __init__(self) -> None:
        super(AudioFrame, self).__init__([128 for _ in range(32)])


def play(
    source: Iterable[AudioFrame],
    wait: bool = True,
    pins: Tuple[_MicroBitAnalogDigitalPin, _MicroBitAnalogDigitalPin] = (pin0, pin1)
) -> None:
    """
    Play the source to completion where 'source' is an iterable, each element
    of which must be an AudioFrame instance.
    """
    pass

# V2

def is_playing() -> None:
    """
    Return True if audio is playing, otherwise return False.
    """
    pass

def stop() -> None:
    """
    Stops all audio playback.
    """
    pass

GIGGLE = None
HAPPY = None
HELLO = None
MYSTERIOUS = None
SAD = None
SLIDE = None
SOARING = None
SPRING = None
TWINKLE = None
YAWN = None
