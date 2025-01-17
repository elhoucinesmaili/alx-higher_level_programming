#!/usr/bin/python3
"""Function that finds a peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    """Function that finds a peak in a list of unsorted integers"""

    if not list_of_integers:
        return None

    # Binary search approach
    low, high = 0, len(list_of_integers) - 1

    while low <= high:
        mid = (low + high) // 2

        # Check if mid is a peak
        if (mid == 0 or list_of_integers[mid - 1] <= list_of_integers[mid]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid + 1] <= list_of_integers[mid]):
            return list_of_integers[mid]

        # Move the search window
        if mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return None  # In case no peak is found, though the problem guarantees a peak

