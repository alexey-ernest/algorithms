"""
Tool for generating random integer array.
"""

import random
import sys

MAX_VALUE = 32767
LENGTH = 10000
if len(sys.argv) > 1:
    LENGTH = int(sys.argv[1])

ITEMS = (random.randrange(0, MAX_VALUE) for i in range(0, LENGTH))
for i in ITEMS:
    print i
