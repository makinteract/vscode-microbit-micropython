from microbit import *
from timer import *

on = False
delay1 = 500
delay2 = 100


def toggleRows(rows):
    global on
    for row in rows:
        for col in range(0, 5):
            if (on):
                display.set_pixel(col, row, 0)  # off
            else:
                display.set_pixel(col, row, 9)  # on
    on = not on


# main

display.clear()

while True:
    # Blink even rows
    tick(delay1, lambda: toggleRows([0, 2, 4]))
    # Blink odd rows
    tick(delay2, lambda: toggleRows([1, 3]))
