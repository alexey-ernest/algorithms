"""
Experiment runner script.
"""

import sortings

DATA_FILE = "data/partial.txt"
ITEMS = [int(i) for i in open(DATA_FILE, "r")]

ITEMS1 = ITEMS[:]
sortings.sort_insertion2(ITEMS1)
print ITEMS1
