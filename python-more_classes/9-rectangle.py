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
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''Sets the width and height attributes'''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        '''print the rectangle with the character "#'''
        if self.width == 0 or self.height == 0:
            return ""

        my_rectangle = ""
        for i in range(self.height):
            my_rectangle += self.width * str(self.print_symbol)
            if i < self.height - 1:
                my_rectangle += "\n"
        return my_rectangle

    def __repr__(self):
        '''Return a string representation that can recreate the object'''
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        '''prints the message when the rectangle is deleted'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @ property
    def width(self):
        '''Gets the width'''
        return self.__width

    @ width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @ property
    def height(self):
        '''Gets the height'''
        return self.__height

    @ height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Calculate the area of a rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''Returns the rectangle perimeter'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @classmethod
    def square(cls, size=0):
        '''returns a new Rectangle instance with width == height == size'''
        width = height = size
        return cls(width, height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''returns the biggest rectangle based on the area'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() != rect_2.area():
            if rect_1.area() > rect_2.area():
                return rect_1
            return rect_2
        return rect_1
