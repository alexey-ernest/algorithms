"""
Tool for generating partial sorted integer array.
"""

import random
import sys

MAX_VALUE = 32767
LENGTH = 10000
if len(sys.argv) > 1:
    LENGTH = int(sys.argv[1])

LAST = 0
ITEMS = []
for i in range(0, LENGTH):
    if random.randrange(0, 100) == 0:
        # 1 percent of random values
        ITEMS.append(random.randrange(0, MAX_VALUE))
    else: 
        LAST += random.randrange(1, 10)
        ITEMS.append(LAST)

for i in ITEMS:
    print i
