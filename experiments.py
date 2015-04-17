"""
Experiment runner script.
"""

import sortings

DATA_FILE = "data/antisorted.txt"
ITEMS = [int(i) for i in open(DATA_FILE, "r")]

sortings.sort_shell(ITEMS)
print ITEMS
