def linear_search(alist, num):
    """
    Return the index of a number in the given list/array
    >>> mylist = [1, 2, 3, 4, 5, 6, 7]
    >>> num = 3  # number to be searched
    >>> linear_search(mylist, num)
    2
    >>>
    """
    for i, elem in enumerate(alist): 
        if elem == num: 
            return i 

    return None  # If number doesn't exist in the list
