#!/usr/bin/env python

from microfs import main
import sys
import os

# This line load the dependencies, prestored in .pip
# sys.path.append(sys.path.append(os.path.abspath('.pip')))
sys.path.append(os.path.abspath('.pip'))
# print(os.path.abspath(''))

main()
