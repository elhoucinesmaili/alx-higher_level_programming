#!/usr/bin/python3

def find_peak(list_of_integers):
    """Find a peak element in a list of unsorted integers."""
    if not list_of_integers:
        return None

    def binary_search_peak(low, high):
        if low == high:
            return list_of_integers[low]
        
        mid = (low + high) // 2

        # Check if the mid-element is a peak
        if list_of_integers[mid] >= list_of_integers[mid - 1] and \
           list_of_integers[mid] >= list_of_integers[mid + 1]:
            return list_of_integers[mid]

        # Move to the left if the left neighbor is greater
        if mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            return binary_search_peak(low, mid - 1)
        else:
            # Move to the right otherwise
            return binary_search_peak(mid + 1, high)

    # Handle edge cases where the list has only one element or two elements
    n = len(list_of_integers)
    if n == 1:
        return list_of_integers[0]
    if n == 2:
        return max(list_of_integers)

    return binary_search_peak(0, len(list_of_integers) - 1)
