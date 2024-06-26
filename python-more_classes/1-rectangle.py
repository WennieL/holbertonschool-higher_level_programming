#!/usr/bin/python3
"""
This is rectangle module that contain an empty class Rectangle
"""


class Rectangle:
    '''
    This defines a rectangle

    Args:
        width: the width of the rectangle
        height: the height of the rectangle

    TypeError: If width or height is not an integer
    ValueError: If width or height is less than zero

    '''

    def __init__(self, width=0, height=0):
        '''Sets the width and height attributes'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Gets the width'''
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Gets the height'''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
