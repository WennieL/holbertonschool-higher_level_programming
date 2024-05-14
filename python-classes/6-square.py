#!/usr/bin/python3
'''This module defines a Square class.'''


class Square:
    '''Represents a square'''

    def __init__(self, size=0, position=(0, 0)):
        '''Initialize a new Square instance.

        Args:
            size: The size of the square.
            position: The position of the square
            '''
        self.size = size
        self.position = position

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
        '''Prints the square with the character #.
        If size is 0, it prints an empty line.
        '''
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                print(" " * self.position[0], end="" + "#" * self.__size)

    @property
    def position(self):
        '''getter the position for the Square'''
        return self.__position

    @position.setter
    def position(self, value):
        '''Setter for the position of the Square with validation.

        Args:
            value(tuple): The position ar which to start printing the square.

        Raisers:
            TypeError: if position is not a tuple of 2 positive integers
        '''
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(num, int) for num in value) \
                or value[0] < 0 or value[1] < 0:
            raise TypeError(
                "position must be a tuple of 2 positive integers")

        self.__position = value
