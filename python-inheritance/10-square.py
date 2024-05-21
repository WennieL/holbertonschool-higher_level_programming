#!/usr/bin/python3
'''
This moudle has a class Square that inderits
frin Rectangle with some methods
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Defines a square class that inherits from Rectangle'''

    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)
