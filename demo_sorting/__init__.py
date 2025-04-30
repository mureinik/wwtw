from typing import List

def qdsort(lst: List[int]):
    """
    A Quick and Dirty Sort algorithm for a list of integers in ascending order
    Nite Owl's implementation: Quicksort
    """
    n = len(lst)
    if n <= 1:
        return lst

    # Find the pivot element
    pivot = lst[n // 2]

    # Partition the list into three parts
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]

    # Recursively sort the left and right parts
    return qdsort(left) + middle + qdsort(right)