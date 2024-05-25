#!/usr/bin/python3
'''
This module contains a function of load_from_json_file
'''

import json


def load_from_json_file(filename):
    '''a function that creates an Object from a “JSON file”'''

    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except PermissionError as e:
        print(f"[PermissionError] {e}")
