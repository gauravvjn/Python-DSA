"""
Sort the array using heap sort algorithm
>>> mylist = [17, 87, 62, 55, 42, 42, 5, 37, 50, 88]
>>> heap_sort(alist)
>>> mylist
[5, 17, 37, 42, 42, 50, 55, 62, 87, 88]
>>>
"""


def heapify(alist, n, i):
    largest = i       # Initialize largest as root
    l = 2 * i + 1     # left = 2 * i + 1
    r = 2 * i + 2     # right = 2 * i + 2

    # See if left child of the node `i` exists and is greater than root
    if l < n and alist[l] > alist[largest]:
        largest = l

    # See if right child of the node `i` exists and is greater than previously found largest number
    if r < n and alist[r] > alist[largest]:
        largest = r

    # If current number is not the largest, we swap it.
    if largest != i:
        alist[i], alist[largest] = alist[largest], alist[i]  # swap
        heapify(alist, n, largest)  # Recursively heapify


def heap_sort(alist):
    n = len(alist)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(alist, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        alist[i], alist[0] = alist[0], alist[i]  # swap
        heapify(alist, i, 0)

    return alist
