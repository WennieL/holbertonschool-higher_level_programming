#!/usr/bin/python3
'''
This module creats an empty class
'''


class BaseGeometry:
    '''This defines BaseGeometry'''

    def area(self):
        '''this get the area'''
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
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        return name, value
