#!/usr/bin/python3
'''
This module contains a function that writes a
string and returns the number of char written
'''


def write_file(filename="", text=""):
    '''the function writes a string and returns the number of chars'''
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return len(text)
