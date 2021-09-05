#!/usr/bin/env python

import sys
import os

# This line load the dependencies, prestored in .pip
# pip install -t .pip -r requirements.txt
# and
# pip3 install -t .pip -r requirements.txt
# from https://medium.com/ovni/pex-python-executables-c0ea39cee7f1
sys.path.append(os.path.abspath('.pip'))

# print(os.path.abspath(''))

# the next line should stay here, after line 8's addition of path
from microfs import main
main()
