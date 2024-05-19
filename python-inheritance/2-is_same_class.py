#!/usr/bin/python3
'''
This module contains a function to check if an object
is exactly an instance of the specified class.
'''


def is_same_class(obj, a_class):
    '''
    a function that returns True if the object is exactly
    an instance of the specified class ; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise.
    '''
    return type(obj) == a_class
