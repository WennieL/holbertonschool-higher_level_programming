#!/usr/bin python3
'''
This mudule create a class named VerboseList
that extends the Python list class. 
This custom class should print a notification
message every time an item is added 
(using the append or extend methods) 
or removed (using the remove or pop methods).
'''
# Notes to myself:
# When you create an instance of a subclass that inherits from a built-in type,
# Python automatically invokes the appropriate constructor of the parent class.
# This initialization process is handled internally by Python,
# so you don't need to explicitly call super().__init__ in your subclass,
# unless you need to perform additional initialization beyond what the parent class provides.


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
        # Nores to myslef:
        # pop(): removes an item at the specified index from the list.
        if index is None:
            item = super().pop()
        else:
            item = super().pop(index)
        print("Popped [{}] from the list.".format(item))
        return item
