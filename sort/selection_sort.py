def selection_sort(alist):
    """
    Sort the array using selection sort algorithm
    >>> mylist = [17, 87, 62, 55, 42, 42, 5, 37, 50, 88]
    >>> selection_sort(mylist)
    >>> mylist
    [5, 17, 37, 42, 42, 50, 55, 62, 87, 88]
    >>>
    """
    n = len(alist)

    for i in range(n):
        # Find the minimum element from index i+1 till last element in the list
        min_index = i
        for j in range(i + 1, n):
            if alist[j] < alist[min_index]:
                min_index = j

        # Swap the minimum element with the first element
        alist[i], alist[min_index] = alist[min_index], alist[i]
