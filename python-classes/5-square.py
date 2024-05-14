#!/usr/bin/python3
'''This module defines a Square class.'''


class Square:
    '''Represents a square'''

    def __init__(self, size=0):
        '''Initialize a new Square instance.

        Args:
            size: The size of the square.
            '''
        self.size = size

    def area(self):
        '''returns area value'''
        return self.__size ** 2

    @property
    def size(self):
        '''getter the size for the Square'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Raises:
        TypeError: if size is not an integer.
        ValueEror: If size if less than 0.
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        '''Prints the square with the character #.'''
        if self.size == 0:
            print("")
        else:
            for _ in range(self.size):
                print("#" * self.size)
