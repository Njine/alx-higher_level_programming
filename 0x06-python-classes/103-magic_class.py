#!/usr/bin/python3
import math


class MagicClass:
    """ create circle area."""

    def __init__(self, r=0):
        """ initializing """
        self.__radius = 0
        if type(r) is not int and type(r) is not float:
            raise TypeError('radius must be a number')
        self.__radius = r

    def circumference(self):
        """ function defining circuference """
        return ((2 * math.pi) * self.__radius)
    
    def area(self):
        """ define area ."""
        return (self.__radius ** 2 * math.pi)

    