"""
sortings.py: standard sorting algorithms (python 2.7).
"""

def sort_selection(items):
    """Sorts an array in place using Selection Sort algorithm.

    Uses ~n**2/2 compares and n (linear!) exchanges to sort collection of length n.

    Args:
        items: array to sort.
    """
    if not items: 
        return

    length = len(items)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if items[j] < items[min_index]:
                min_index = j
        _exchange(items, i, min_index)

def sort_insertion(items):
    """Sorts an array in place using Insertion Sort algorithm.

    Uses ~n**2/4 compares and ~n**2/4 exchanges to sort a randomly ordered 
    array of length n with distinct keys, on the average. The worst case is 
    ~n**2/2 compares and ~n**2/2 exchanges and the best case is n-1 compares
    and 0 exchanges.

    Best for: array where each entry is not far from its final position
              a small array appended to a large sorted array
              an array with only a few entries that are not in place

    Args:
        items: array to sort.
    """
    if not items:
        return
    
    length = len(items)
    for i in range(1, length):
        for j in range(i, 0, -1):
            if items[j] >= items[j - 1]:
                break
            _exchange(items, j, j - 1)

def sort_insertion2(items):
    """Sorts an array in place using improved Insertion Sort algorithm.

    Number of array accesses is reduced twice.

    Args:
        items: array to sort.
    """
    if not items:
        return
    
    length = len(items)
    for i in range(1, length):
        insert_index = 0
        item = items[i]
        for j in range(i, 0, -1):
            if item >= items[j - 1]:
                insert_index = j
                break
            items[j] = items[j - 1]
        items[insert_index] = item

def sort_shell(items):
    """Sorts an array in place using Shellsort algorithm.

    Improves Insertion Sort algorithm by deviding array into subsequences.

    Args:
        items: array to sort.
    """
    length = len(items)
    
    # Calculating incrementing sequence (h in literature): 1, 4, 13, 40, 121, 364, 1093, ...
    inc_seq = 1
    while inc_seq < length // 3:
        inc_seq = 3*inc_seq + 1

    while inc_seq >= 1:
        # h-sort the array.
        for i in range(inc_seq, length):
            for j in range(i, inc_seq-1, -inc_seq):
                # insert items[i] among items[i-h], items[i-2*h], items[i-3*h]... .
                if items[j] >= items[j-inc_seq]:
                    break
                _exchange(items, j, j-inc_seq)
        inc_seq = inc_seq // 3

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

