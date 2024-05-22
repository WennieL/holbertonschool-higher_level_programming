#!/usr/bin/python3
'''
Design two mixin classes, SwimMixin and FlyMixin, 
each equipped with methods swim and fly respectively. 
Next, construct a class Dragon that inherits from both these mixins. 
Your aim is to show that a Dragon instance can both swim and fly.
'''


class SwimMixin:
    '''Mixin class for swimming capability'''

    def swim(self):
        '''swim method'''
        print("The creature swims!")


class FlyMixin:
    '''Mixin class for flying capability'''

    def fly(self):
        '''fly method'''
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    '''Class representing a dragon, inheriting swim and fly capabilities'''

    def roar(self):
        '''roar function'''
        print("The dragon roars!")
