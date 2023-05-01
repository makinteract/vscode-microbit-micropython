# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from typing import (
    List,
    Tuple,
    Union,
)

from microbit import (
    _MicroBitAnalogDigitalPin,
    pin0,
)

_MusicalNote = str
_Music = List[_MusicalNote]


def set_tempo(number: int, bpm: int) -> None:
    """
    Make a beat last a 'number' of ticks long and played at 'bpm' beats per
    minute.
    """
    pass


def pitch(
    freq: int,
    length: int = -1,
    pin: _MicroBitAnalogDigitalPin = pin0,
    wait: bool = True,
) -> None:
    """
    Make micro:bit play a note at 'freq' frequency for 'length' milliseconds.
    E.g. pitch(440, 1000) will play concert 'A' for 1 second.
    If length is a negative number the pitch is played continuously.
    Use the optional pin argument to override the default output for the
    speaker.
    If wait is False the music will play in the background while the program
    continues.
    """
    pass


def play(
    music: Union[_Music, _MusicalNote],
    pin: _MicroBitAnalogDigitalPin = pin0,
    wait: bool = True,
    loop: bool = False,
) -> None:
    """
    Make micro:bit play 'music' list of notes. Try out the built in music to
    see how it works. E.g. music.play(music.PUNCHLINE).
    Use the optional pin argument to override the default output for the
    speaker.
    If wait is False the music will play in the background while the program
    continues.
    If loop is True, the tune will repeat.
    """
    pass


def get_tempo() -> Tuple[int, int]:
    """
    Return the number of ticks in a beat and number of beats per minute.
    """
    pass


def stop(pin: _MicroBitAnalogDigitalPin = pin0) -> None:
    """
    Stops all music playback on the given pin.
    If no pin is given, pin0 is assumed.
    """
    pass


def reset() -> None:
    """
    If things go wrong, reset() the music to its default settings.
    """
    pass


DADADADUM = None
ENTERTAINER = None
PRELUDE = None
ODE = None
NYAN = None
RINGTONE = None
FUNK = None
BLUES = None
BIRTHDAY = None
WEDDING = None
FUNERAL = None
PUNCHLINE = None
PYTHON = None
BADDY = None
CHASE = None
BA_DING = None
WAWAWAWAA = None
JUMP_UP = None
JUMP_DOWN = None
POWER_UP = None
POWER_DOWN = None