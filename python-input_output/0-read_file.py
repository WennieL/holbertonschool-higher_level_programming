#!/usr/bin/python3
'''
This module contain a function that reads a text file and print it
'''


def read_file(filename=""):
    '''a function that reads a text file (UTF8) and prints it to stdout:'''
    with open(filename) as f:
        print(f.read().rstrip())
