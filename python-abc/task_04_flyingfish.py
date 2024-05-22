#!/usr/bin/python3
'''
Construct a FlyingFish class that inherits from
both a Fish class and a Bird class. Within FlyingFish,
override methods from both parents.
The goal is to comprehend multiple inheritance
and how Python determines method resolution order.
'''


class Fish:
     '''Defines a Fish class'''

    def swim(self):
        '''swom method'''
        print("The fish is swimming")

    def habitat(self):
        '''habitat method'''
        print("The fish lives in water")


class Bird:
    '''Defines a Bird class'''

    def fly(self):
        '''fly method'''
        print("The bird is flying")

    def habitat(self):
        '''habitate method'''
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    '''Defines a FlyingFish class inheriting from Fish and Bird'''

    def fly(self):
        '''Override fly method'''
        print("The flying fish is soaring!")

    def swim(self):
        '''Override swim method'''
        print("The flying fish is swimming!")

    def habitat(self):
        '''Override habitat method'''
        print("The flying fish lives both in water and the sky!")
