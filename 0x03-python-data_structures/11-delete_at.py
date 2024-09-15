#!/usr/bin/python3
def delete_at(my_list=[], i=0):
    if i < 0 or i > len(my_list) - 1:
        return my_list
    else:
        del my_list[i]
    return my_list
