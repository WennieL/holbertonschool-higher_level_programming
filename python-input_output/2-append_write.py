#!/usr/bin/python3
'''
This module contains a function that appends a str
and return the len of chars added
'''


def append_write(filename="", text=""):
    '''
    a function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added:
    '''
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return len(text)
