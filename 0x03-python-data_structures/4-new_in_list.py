#!/usr/bin/python3

def new_in_list(my_list, i, element):
    copy = my_list.copy()
    if i < 0 or i > len(my_list) - 1:
        return my_list.copy()
    else:
        copy[i] = element
        return copy
