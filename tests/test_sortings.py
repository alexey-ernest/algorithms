"""
Sorting algorithms tests.
"""

import unittest
import sortings

class SelectionSortTest(unittest.TestCase):
    """
    Selection Sort tests.
    """

    def test_selection(self):
        """Selection test.
        """
        self.assertEquals(sortings.sort_selection([2, 1, 3]), list(range(1, 4)))

class InsertionSortTest(unittest.TestCase):
    """
    Insertion Sort tests.
    """

    def test_insertion(self):
        """Insertion Sort.
        """
        self.assertEquals(sortings.sort_insertion([2, 1, 3]), list(range(1, 4)))

    def test_insertion2(self):
        """Improved Insertion Sort.
        """
        self.assertEquals(sortings.sort_insertion2([2, 1, 3, 5, 4, 8, 6, 7]), list(range(1, 9)))

    def test_antisorted(self):
        """Sorts antisorted array using Insertion Sort algorithm.
        """
        items = range(10)
        self.assertEquals(sortings.sort_insertion(list(reversed(items))), items)

if __name__ == "__main__":
    unittest.main()  
