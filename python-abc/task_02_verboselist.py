#!/usr/bin python3
'''
This mudule create a class named VerboseList
that extends the Python list class. 
This custom class should print a notification
message every time an item is added 
(using the append or extend methods) 
or removed (using the remove or pop methods).
'''


class VerboseList(list):
    '''A subclass of list that prints messages on modifications'''

    def append(self, item):
        '''Appends an item to the list and prints a message'''
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item):
        '''Extends the list with items and prints a message'''
        super().extend(item)
        print("Extended the list with [{}] items.".format(len(item)))

    def remove(self, item):
        '''Removes an item from the list and prints a message'''
        super().remove(item)
        print("Removed [{}] from the list.".format(item))

    def pop(self, index=None):
        '''Pops an item from the list and prints a message'''
        if index is None:
            item = super().pop()
            print("Popped [{}] from the list.".format(item))
        else:
            item = super().pop(index)
            print("Popped [{}] from the list.".format(item))
