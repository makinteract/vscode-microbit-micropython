#!/usr/bin/env python

import sys
import os

# This line load the dependencies, prestored in .pip
# sys.path.append(sys.path.append(os.path.abspath('.pip')))
sys.path.append(os.path.abspath('.pip'))
# print(os.path.abspath(''))

# the next line should stay here, after line 8's addition of path
from microfs import main
main()
