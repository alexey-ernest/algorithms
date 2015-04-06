"""
Standard sorting algorithms
"""

def selection_sort(items):
    """Sorts an iterable collection using Selection Sort algorithm.

    Args:
        items: iterable collection to sort.

    Returns:
        Sorted collection.
    """
    if not items: 
        return []
    
    def exchange(items, i, j):
        """Exchanges values in collection.

    	Args:
    		items: indexing collection.
    		i: first item index.
    		j: second item index.
    	"""
        tmp = items[i]
        items[i] = items[j]
        items[j] = tmp

    length = len(items)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if items[j] < items[min_index]:
                min_index = j
        exchange(items, i, min_index)
    return items


