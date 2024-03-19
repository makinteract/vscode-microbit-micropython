# Music

""" This is the music module and you can use it to create and play melodies. 
By default sound output will be via the edge connector on pin 0 and the 
built-in speaker V2.  """

# Musical Notation

""" An individual note is specified thus:
Note[octave][:duration]
For example, A1:4 refers to the note “A” in octave 1 that lasts for four 
ticks (a tick is an arbitrary length of time defined by a tempo setting 
function - see below). If the note name R is used then it is treated as a 
rest (silence).

Accidentals (flats and sharps) are denoted by the b (flat - a lower case b) 
and # (sharp - a hash symbol). For example, Ab is A-flat and C# is C-sharp. """


# Functions

def set_tempo(ticks=4, bpm=120):
    """ Sets the approximate tempo for playback.
    A number of ticks (expressed as an integer) constitute a beat. Each 
    beat is to be played at a certain frequency per minute (expressed as 
    the more familiar BPM - beats per minute - also as an integer).

    Suggested default values allow the following useful behaviour:

        set_tempo() - reset the tempo to default of ticks = 4, bpm = 120
        set_tempo(ticks=8) - change the “definition” of a beat
        set_tempo(bpm=180) - just change the tempo

    To work out the length of a tick in milliseconds is very simple arithmetic:
    60000/bpm/ticks_per_beat . For the default values that’s 
    60000/120/4 = 125 milliseconds or 1 beat = 500 milliseconds. """
    pass

def get_tempo():
    """ Gets the current tempo as a tuple of integers: (ticks, bpm). """
    pass

def play(music, pin=pin0, wait=True, loop=False):
    """ Plays music containing the musical DSL defined above.
    If music is a string it is expected to be a single note such as, 'c1:4'.
    If music is specified as a list of notes (as defined in the section on 
    the musical DSL, above) then they are played one after the other to 
    perform a melody.
    In both cases, the duration and octave values are reset to their defaults 
    before the music (whatever it may be) is played.
    An optional argument to specify the output pin can be used to override 
    the default of microbit.pin0. If we do not want any sound to play we can 
    use pin=None.
    If wait is set to True, this function is blocking.
    If loop is set to True, the tune repeats until stop is called (see below) 
    or the blocking call is interrupted. """
    pass

def pitch(frequency, duration=-1, pin=pin0, wait=True):
    """ Plays a pitch at the integer frequency given for the specified number 
    of milliseconds. For example, if the frequency is set to 440 and the 
    length to 1000 then we hear a standard concert A for one second.
    Note that you can only play one pitch on one pin at any one time.
    An optional argument to specify the output pin can be used to override 
    the default of microbit.pin0. If we do not want any sound to play out of 
    the pins we can use pin=None.
    If wait is set to True, this function is blocking.
    If duration is negative the pitch is played continuously until either 
    the blocking call is interrupted or, in the case of a background call, 
    a new frequency is set or stop is called (see below). """
    pass

def stop(pin=pin0):
    """ Stops all music playback on the built-in speaker and any pin 
    outputting sound. An optional argument can be provided to specify 
    a pin, eg. stop(pin1). """
    pass

def reset():
   """  Resets the state of the following attributes in the following way:

            ticks = 4
            bpm = 120
            duration = 4
            octave = 4 """
   pass

# Built in Melodies

""" For the purposes of education and entertainment, the module contains 
several example tunes that are expressed as Python lists. They can be used 
like this:

    import music
    play(NYAN)

All the tunes are either out of copyright, composed by Nicholas H.Tollervey 
and released to the public domain or have an unknown composer and are covered 
by a fair (educational) use provision.

They are: """

DADADADUM = None #- the opening to Beethoven’s 5th Symphony in C minor.
ENTERTAINER = None #- the opening fragment of Scott Joplin’s Ragtime classic “The Entertainer”.
PRELUDE = None #- the opening of the first Prelude in C Major of J.S.Bach’s 48 Preludes and Fugues.
ODE = None #- the “Ode to Joy” theme from Beethoven’s 9th Symphony in D minor.
NYAN = None #- the Nyan Cat theme (http://www.nyan.cat/). The composer is unknown. This is fair use for educational porpoises (as they say in New York).
RINGTONE = None #- something that sounds like a mobile phone ringtone. To be used to indicate an incoming message.
FUNK = None #- a funky bass line for secret agents and criminal masterminds.
BLUES = None #- a boogie-woogie 12-bar blues walking bass.
BIRTHDAY = None #- “Happy Birthday to You…” for copyright status see: http://www.bbc.co.uk/news/world-us-canada-34332853
WEDDING = None #- the bridal chorus from Wagner’s opera “Lohengrin”.
FUNERAL = None #- the “funeral march” otherwise known as Frédéric Chopin’s Piano Sonata No. 2 in B♭ minor, Op. 35.
PUNCHLINE = None #- a fun fragment that signifies a joke has been made.
PYTHON = None #- John Philip Sousa’s march “Liberty Bell” aka, the theme for “Monty Python’s Flying Circus” (after which the Python programming language is named).
BADDY = None #- silent movie era entrance of a baddy.
CHASE = None #- silent movie era chase scene.
BA_DING = None #- a short signal to indicate something has happened.
WAWAWAWAA = None #- a very sad trombone.
JUMP_UP = None #- for use in a game, indicating upward movement.
JUMP_DOWN = None #- for use in a game, indicating downward movement.
POWER_UP = None #- a fanfare to indicate an achievement unlocked.
POWER_DOWN = None #- a sad fanfare to indicate an achievement lost.
