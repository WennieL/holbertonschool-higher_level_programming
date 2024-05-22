#!/usr/bin/python3
'''
This module creates an abstract class named Animal using the
ABC package.
'''
from abc import ABC, abstractmethod


class Animal(ABC):
    '''This defines an abstract class Animal'''

    @abstractmethod
    def sound(self):
        '''Abstract method for sound, must be implemented by subclasses'''
        pass


class Dog(Animal):
    '''This is a subclass of Animal representing a dog'''

    def sound(self):
        '''
        the sound method for the Dog class and
        it returns the string “Bark”.
        '''
        return "Bark"


class Cat(Animal):
    '''This is a subclass of Animal representing a cat'''

    def sound(self):
        '''
        the sound method for the Cat class and
        it returns the string “Meow”.
        '''
        return "Meow"
