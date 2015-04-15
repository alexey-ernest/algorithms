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
        """Selection Sort.
        """
        items = [2, 1, 3]
        sortings.sort_selection(items)
        self.assertEquals(items, range(1, 4))

class InsertionSortTest(unittest.TestCase):
    """
    Insertion Sort tests.
    """

    def test_insertion(self):
        """Insertion Sort.
        """
        items = [2, 1, 3]
        sortings.sort_insertion(items)
        self.assertEquals(items, range(1, 4))

    def test_insertion2(self):
        """Improved Insertion Sort.
        """
        items = [2, 1, 3, 5, 4, 8, 6, 7]
        sortings.sort_insertion2(items)
        self.assertEquals(items, range(1, 9))

    def test_antisorted(self):
        """Insertion Sort for anti-ordered array.
        """
        items = range(9, -1, -1)
        sortings.sort_insertion(items)
        self.assertEquals(items, range(10))

class ShellSorttest(unittest.TestCase):
    """
    Shellsort tests.
    """

    def test_shell(self):
        """Shell h-sort.
        """
        items = ['S', 'H', 'E', 'L', 'L', 'S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
        sortings.sort_shell(items)
        self.assertEquals(
            items, 
            ['A', 'E', 'E', 'E', 'H', 'L', 'L', 'L', 'M', 'O', 'P', 'R', 'S', 'S', 'T', 'X'])

if __name__ == "__main__":
    unittest.main()  
