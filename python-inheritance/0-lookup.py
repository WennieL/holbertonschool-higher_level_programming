#!/usr/bin/python3
'''This module is to lookup the available
attributes and methods of an object '''


def lookup(obj):
    '''
    a function that returns the list of
    available attributes and methods of an object:
    '''
    return dir(obj)
