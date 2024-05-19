#!/usr/bin/python3
'''
This module contains a function to check if an object
is an instance of a class that inherited from, the specified class
'''


def is_kind_of_class(obj, a_class):
    '''
    a function that returns True if the object
    is an instance of, or if the object is an
    instance of a class that inherited from,
    the specified class ; otherwise False

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise.
    '''
    return isinstance(obj, a_class)
