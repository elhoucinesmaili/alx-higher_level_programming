#!/usr/bin/python3

def replace_in_list(my_list, i, element):
    if i < 0 or i > len(my_list) - 1:
        return my_list
    else:
        my_list[i] = element
        return my_list
