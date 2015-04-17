"""
Tool for generating anti-sorted array.
"""

import random
import sys

LENGTH = 10000
if len(sys.argv) > 1:
    LENGTH = int(sys.argv[1])

LAST = 0
ITEMS = []
for i in range(0, LENGTH):
    LAST += random.randrange(1, 97)
    ITEMS.append(LAST)

for i in reversed(ITEMS):
    print i
