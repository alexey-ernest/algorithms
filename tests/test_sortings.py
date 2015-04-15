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
        self.assertEquals(sortings.selection_sort([2, 1, 3]), [1, 2, 3])

class InsertionSortTest(unittest.TestCase):
    """
    Insertion Sort tests.
    """

    def test_insertion(self):
        """Insertion test.
        """
        self.assertEquals(sortings.insertion_sort([2, 1, 3]), [1, 2, 3])

    def test_antisorted(self):
        """Sorts anti-ordered array using Insertion Sort algorithm.
        """
        items = range(10)
        self.assertEquals(sortings.insertion_sort(list(reversed(items))), items)        

if __name__ == "__main__":
    unittest.main()
