#!/usr/bin/python3
'''
This moudle has a class Square that inherits
from Rectangle with some methods
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Defines a square class that inherits from Rectangle'''

    def __init__(self, size):
        '''Initializes a square with size
        validating the size value first
        to catch any invalid values early
        '''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
