#!/usr/bin/python3
"""2-square.py: Defines size as an int and also greater than 0."""


class Square:
    """Creates  Square type."""

    def __init__(self, size=0):
        """Initialize Square with dime."""
        self.__size = size
        if type(size) is not int:
            raise TypeError('dime must be an integer')
        if size < 0:
            raise ValueError('dime must be >= 0')
