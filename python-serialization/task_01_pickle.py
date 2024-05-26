#!/bin.usr/python3
'''
This module uses pickle to serialize and deserialize custom Python objects
'''
import json
import pickle


class CustomObject:
    '''
    A custom class

    Args:
        name (a string)
        age (an integer)
        is_student (a boolean)
    '''

    def __init__(self, name, age, is_student):
        self.name = str(name)
        self.age = int(age)
        self.is_student = bool(is_student)

    def display(self):
        '''print out the object's attributes'''
        print(
            f"Name: {self.name}\nAge: {self.age}\
            \nIs Student: {self.is_student}")

    def serialize(self, filename):
        '''
        This method will take a filename as its parameter.
        Using the pickle module, it will serialize the current
        instance of the object and save it to the provided filename.
        '''
        try:
            with open(filename, "wb") as jfile:
                pickle.dump(self, jfile)
        except Exception as e:
            print(f"{e}")

    @classmethod
    def deserialize(cls, filename):
        '''
        This class method will take a filename as its parameter.
        Using the pickle module, it will load and return an instance
        of the CustomObject from the provided filename.
        '''
        try:
            with open(filename, "rb") as pyfile:
                return pickle.load(pyfile)
        except (FileNotFoundError, pickle.UnpicklingError) as e:
            print(f"{e}")
            return None


# Create an instance of CustomObject
obj = CustomObject(name="John", age=25, is_student=True)
print("Original Object:")
obj.display()

# Serialize the object
obj.serialize("object.pkl")

# Deserialize the object into a new instance
new_obj = CustomObject.deserialize("object.pkl")
print("\nDeserialized Object:")
new_obj.display()
