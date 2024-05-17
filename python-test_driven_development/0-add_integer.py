#!/usr/bin/python3
"""
This module provides a function to add two integers or floats.
"""


def add_integer(a, b=98):
    """
    Add two integers or floats and return the sum as an integer.\

    Args:
        a: first interger, must be an integer or float
        b: second integer, must be an integer or float. Default value is 98

    Returns:
        The sum of a and b as an integer.

    Raises:
    TypeError: If a or b are not integers or floats.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
