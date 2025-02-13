uFlash
======

**THIS MODULE ONLY WORKS WITH PYTHON 2.7 or 3.3+.**

A utility for flashing the BBC micro:bit with Python scripts and the
MicroPython runtime. You pronounce the name of this utility "micro-flash". ;-)

It provides three services:

1. A library of functions to programatically create a hex file and flash it onto a BBC micro:bit.
2. A command line utility called `uflash` that will flash Python scripts onto a BBC micro:bit.
3. A command line utility called `py2hex` for creating hex files from Python scripts and saving them on the local filesystem

Several essential operations are implemented:

* Encode Python into the hex format.
* Embed the resulting hexified Python into the MicroPython runtime hex.
* Extract an encoded Python script from a MicroPython hex file.
* Discover the connected micro:bit.
* Copy the resulting hex onto the micro:bit, thus flashing the device.
* Specify the MicroPython runtime hex in which to embed your Python code.

Installation
------------

To install simply type::

    $ pip install uflash

...and the package will download from PyPI. If you wish to upgrade to the
latest version, use the following command::

    $ pip install --no-cache --upgrade uflash

**NB:** You must use a USB *data* cable to connect the micro:bit to your
computer (some cables are power only). You're in good shape if, when plugged
in, the micro:bit appears as a USB storage device on your file system.

Linux users: For uflash to work you must ensure the micro:bit is mounted as a
USB storage device. Usually this is done automatically. If not you've probably
configured automounting to be off. If that's the case, we assume you
have the technical knowledge to mount the device yourself or to install the
required kernel modules if they're missing. Default installs of popular Linux
distros "should just work" (tm) out of the box given a default install.

Command Usage
-------------

uflash
~~~~~~

To read help simply type::

    $ uflash --help

or::

    $ uflash -h

To discover the version information type::

    $ uflash --version

If you type the command on its own then uflash will attempt to find a connected
BBC micro:bit and flash an unmodified default version of the MicroPython
runtime onto it::

    $ uflash
    Flashing Python to: /media/ntoll/MICROBIT/micropython.hex

To flash a version of the MicroPython runtime with a specified script embedded
within it (so that script is run when the BBC micro:bit boots up) then pass
the path to the Python script in as the first argument to the command::

    $ uflash my_script.py
    Flashing my_script.py to: /media/ntoll/MICROBIT/micropython.hex

You can let uflash watch for changes of your script. It will be flashed
automatically every time you save it::

    $ uflash -w my_script.py

or::

    $ uflash --watch my_script.py

At this point uflash will try to automatically detect the path to the device.
However, if you have several devices plugged in and/or know what the path on
the filesystem to the BBC micro:bit already is, you can specify this as a
second argument to the command::

    $ uflash myscript.py /media/ntoll/MICROBIT
    Flashing myscript.py to: /media/ntoll/MICROBIT/micropython.hex

You can even flash multiple devices at once::

    $ uflash myscript.py /media/ntoll/MICROBIT /media/ntoll/MICROBIT1
    Flashing myscript.py to: /media/ntoll/MICROBIT/micropython.hex
    Flashing myscript.py to: /media/ntoll/MICROBIT1/micropython.hex

To extract a Python script from a hex file use the "-e" flag like this::

    $ uflash -e something.hex myscript.py

This will save the Python script recovered from "something.hex" into the file
"myscript.py". If you don't supply a target the recovered script will emit to
stdout.

If you're developing MicroPython and have a custom runtime hex file you can
specify that uflash use it instead of the built-in version of MicroPython in
the following way::

    $ uflash -r firmware.hex

or::

    $ uflash --runtime=firmware.hex

py2hex
~~~~~~

To create output .hex files in the same directory as the input .py files::

   $ py2hex tests/example.py
   Hexifying example.py as: tests/example.hex

py2hex includes that same -r/--runtime and -m/--minify options as uflash
and adds an additional option -o/--outdir:

To create output .hex files in a different directory::

   $ py2hex example.py -o /tmp
   Hexifying example.py as: /tmp/example.hex

or::

   $ py2hex example.py --outdir /tmp
   Hexifying example.py as: /tmp/example.hex

py2hex can handle multiple input files::

   $ py2hex a.py b.py c.py
   Hexifying a.py as: a.hex
   Hexifying b.py as: b.hex
   Hexifying c.py as: c.hex

or::

   $ py2hex *.py
   Hexifying a.py as: a.hex
   Hexifying b.py as: b.hex
   Hexifying c.py as: c.hex

Development
-----------

The source code is hosted in GitHub. Please feel free to fork the repository.
Assuming you have Git installed you can download the code from the canonical
repository with the following command::

    $ git clone https://github.com/ntoll/uflash.git

Ensure you have the correct dependencies for development installed by creating
a virtualenv and running::

    $ pip install -r requirements.txt

To locally install your development version of the module into a virtualenv,
run the following command::

    $ python setup.py develop

There is a Makefile that helps with most of the common workflows associated
with development. Typing ``make`` on its own will list the options thus::

    $ make

    There is no default Makefile target right now. Try:

    make clean - reset the project and remove auto-generated assets.
    make pyflakes - run the PyFlakes code checker.
    make pep8 - run the PEP8 style checker.
    make test - run the test suite.
    make coverage - view a report on test coverage.
    make check - run all the checkers and tests.
    make package - create a deployable package for the project.
    make rpm - create an rpm package for the project.
    make publish - publish the project to PyPI.
    make docs - run sphinx to create project documentation.
