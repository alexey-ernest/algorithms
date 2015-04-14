"""
Standard sorting algorithms.
"""

def selection_sort(items):
    """Sorts an array in place using Selection Sort algorithm.

    Uses ~n**2/2 compares and n exchanges to sort collection of length n.

    Args:
        items: array to sort.

    Returns:
        Sorted array.
    """
    if not items: 
        return []

    length = len(items)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if items[j] < items[min_index]:
                min_index = j
        _exchange(items, i, min_index)
    return items

def insertion_sort(items):
    """Sorts an array in place using Insertion Sort algorithm.

    Uses ~n**2/4 compares and ~n**2/4 exchanges to sort a randomly ordered 
    array of length n with distinct keys, on the average. The worst case is 
    ~n**2/2 compares and ~n**2/2 exchanges and the best case is n-1 compares
    and 0 exchanges.

    Args:
        items: array to sort.

    Returns:
        Sorted array.
    """
    if not items:
        return []
    
    length = len(items)
    for i in range(1, length):
        for j in reversed(range(1, i + 1)):
            if items[j] >= items[j - 1]:
                break
            _exchange(items, j, j - 1)
    return items

def _exchange(items, i, j):
    """Exchanges values in collection.

	Args:
		items: indexing collection.
		i: first item index.
		j: second item index.
	"""
    tmp = items[i]
    items[i] = items[j]
    items[j] = tmp

