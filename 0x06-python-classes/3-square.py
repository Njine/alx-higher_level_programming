#!/usr/bin/python3
'''3-square.py: Defines Area that returns the current square area'''


class Square:
    """Creates  Square type."""

    def __init__(self, dime=0):
        """Initialize Square with size."""
        self.__size = dime
        if type(dime) is not int:
            raise TypeError('size must be an integer')
        if dime < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """Define the area of a square."""
        return self.__size * self.__size
