#!/usr/bin/python3
'''
This module defines a class Stuent
'''


class Student:
    '''
    Creates a class

    Args:
        first_name: first attribute
        last_name: second attribute
        age: thirdattribute
    '''

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''retrieves a dictionary representation of a Student instance'''

        return (self.__dict__)
