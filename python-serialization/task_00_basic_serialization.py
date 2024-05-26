#!/usr/bin/python3

'''
this module adds the functionality to serialize a Python dictionary
to a JSON file and deserialize the JSON file
to recreate the Python Dictionary.
'''
import json


def serialize_and_save_to_file(data, filename):
    '''
    A function that serialize a Python dictionary to a JSON file

    Args:
        data: A Python Dictionary with data
        filename: The filename of the output JSON file
        If the output file already exists it should be replaced.
    '''
    with open(filename, "w", encoding="utf-8") as jfile:
        json.dump(data, jfile)


def load_and_deserialize(filename):
    '''
    A functin that deserialize the JSON file to recreate the Python Dictionary.

    Args:
        filename: The filename of the input JSON file This function returns
        a Python Dictionary with the deseialized JSON data from the file.

    '''
    with open(filename, "r", encoding="utf-8") as pyfile:
        return json.load(pyfile)
