#!/usr/bin/python3
"""2-square.py: Defines size as an int and also greater than 0."""


class Square:
    """Creates  Square type."""

    def __init__(self, dime=0):
        """Initialize Square with dime."""
        self.__size = dime
        if type(dime) is not int:
            raise TypeError('dime must be an integer')
        if dime < 0:
            raise ValueError('dime must be >= 0')
