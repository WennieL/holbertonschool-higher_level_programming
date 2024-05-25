#!/usr/bin/python3
'''
This module contains a function that writes
and Obj to a text file with JSON repr
'''
import json


def save_to_json_file(my_obj, filename):
    '''
    A function that writes an object to a text file,
    using a JSON representation.
    '''

    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(my_obj, f)
    except PermissionError as e:
        print(f"[PermissionError] {e}")
