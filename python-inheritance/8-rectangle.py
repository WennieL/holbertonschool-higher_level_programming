#!/usr/bin/python3
'''
This module creats an empty class
'''


class BaseGeometry:
    '''This defines BaseGeometry'''

    def area(self):
        '''returns area'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        Validates that a value is a positive integer.

        Args:
            name (str): The name of the value (used in error messages).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to zero.
        '''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    '''Rectangle inherits from BaseGeometry'''

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
