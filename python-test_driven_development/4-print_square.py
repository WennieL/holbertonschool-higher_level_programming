#!/usr/bin/python3
'''
This module prints a square with the character #.
'''


def print_square(size):
    """
    A funvtion that prints a square with the character #.

    Args:
        size: the size length of the square

    Raises:
        TypeError: If size is not an integer,
                   or is size is a float and is less than zero
        ValueError: If size is less than zero

    """

    if not isinstance(size, int):
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        else:
            raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print(size * "#")
