#!/usr/bin/python3
'''
This module defines a subclass of the built-in list, providing additional functionality to print the list in sorted order.
'''


class MyList(list):
    '''A subclass of list that includes a method to
    print the list in sorted order'''

    def print_sorted(self):
        '''Prints the list in ascending order'''
        new_list = sorted(self)
        print(new_list)
