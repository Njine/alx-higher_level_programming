#!/usr/bin/python3
"""2-square.py: Defines size as an int and also >= 0."""


class Square:
    """Creates  Square type."""

    def __init__(self, dime=0):
        """Initialize Square with dime."""
        self.__size = dime
        if type(dime) is not int:
            raise TypeError('size must be an integer')
        if dime < 0:
            raise ValueError('size must be >= 0')
