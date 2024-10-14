#!/usr/bin/python3
"""
This module contains the function is_same_class
"""

def is_same_class(obj, a_class):
    '''Determines if an object is exactly an instance of a specified class.'''
    return type(obj) == a_class
