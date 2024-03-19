#LOGS

""" This module lets you log data to a ``MY_DATA`` file saved on a micro:bit
**V2** ``MICROBIT`` USB drive.

The data is structured in a table format and it can be viewed and plotted with
a browser.

Further guidance on this feature can be found on the
`data logging page of the microbit.org website
<https://microbit.org/get-started/user-guide/data-logging/>`_.
"""

# Functions

def set_labels(*labels, timestamp=log.SECONDS):
    """  Set up the log file header. """

def set_mirroring(serial):
    """ Configure mirroring of the data logging activity to the serial output."""

def delete(full=False):
    """ Delete the contents of the log, including headers. """

def add( data_dictionary, /, *, **kwargs)
    """ Add a data row to the log. """


   
  