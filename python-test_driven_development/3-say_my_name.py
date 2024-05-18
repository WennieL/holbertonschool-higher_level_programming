#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix..
"""


def say_my_name(first_name, last_name=""):
    """
    A funvtion that prints My name is <first name> <last name>

    Args:
        first name: must be strings.
        last name: must be strings.

    Raises:
        TypeError: If first_name or last_name is not a string.

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f'My name is {first_name} {last_name}')
