import sys
import platform
import sysconfig
import os
import time
from time import gmtime, strftime
import datetime

# Architecture
print("Architecture: " + platform.architecture()[0])

# machine
print("Machine: " + platform.machine())

# node
print("Node: " + platform.node())

# system
print("System: " + platform.system())

# distribution
dist = platform.dist()
dist = " ".join(x for x in dist)
print("Distribution: " + dist)





