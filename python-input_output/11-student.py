#!/usr/bin/python3
'''This module is based on 9-student.py'''


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

    def to_json(self, attrs=None):
        '''retrieves a dictionary representation of a Student instance'''
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        '''replaces all attributes of the Student instance'''
        for key, value in json.items():
            setattr(self, key, value)
