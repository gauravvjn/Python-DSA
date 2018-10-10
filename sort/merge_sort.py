"""
Sort the array using merge sort algorithm
>>> mylist = [17, 87, 62, 55, 42, 42, 5, 37, 50, 88]
>>> merge_sort(mylist)
>>> mylist
[5, 17, 37, 42, 42, 50, 55, 62, 87, 88]
>>>
"""


def merge_sort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2  # Mid of the array
        left_list = alist[:mid]  # Creating another list for first half
        right_list = alist[mid:]  # Creating another list for second half

        merge_sort(left_list)  # Sorting the left list recursively
        merge_sort(right_list)  # Sorting the right list recursively

        i = j = k = 0

        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                alist[k] = left_list[i]
                i += 1
            else:
                alist[k] = right_list[j]
                j += 1
            k += 1

        # Remaining elements
        while i < len(left_list):
            alist[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            alist[k] = right_list[j]
            j += 1
            k += 1
