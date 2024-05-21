#!/usr/bin/python3
'''
This moudle has a class Rectangle that inderits
frin BaseGeometry with some methods
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Defines a rectangle class that inherits from BaseGeometry'''

    def __init__(self, width, height):
        '''Instantiation with width and height'''
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)

    def area(self):
        '''return value of the area'''
        return (self.__width * self.__height)

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
