#!/usr/bin/env python

import sys
import os

# This line load the dependencies, prestored in .pip
sys.path.append(sys.path.append(os.path.abspath('.pip')))

from microfs import main
main()
