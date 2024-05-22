#!/usr/bin/pyhhon3
'''
This module create an abstract class
named Shape with two abstract methods.
'''

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    '''Abstract class named Shape'''

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    '''This is a subclass of Shape'''

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        '''returns the value of the area of a Circle'''
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        '''returns the value of the perimeter of a Circle'''
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    '''This is a subclass of Rectangle'''

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        '''returns the value of the area of a Rectangle'''
        return self.width * self.height

    def perimeter(self):
        '''returns the value of perimeter of a Rectangle'''
        return 2 * (self.width + self.height)


def shape_info(shape):
    '''this prints its area and perimeter'''

    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
