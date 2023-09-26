#!/usr/bin/python3
"""2-square.py: Defines size as an int and also greater or equal to 0."""


class Square:
    """Creates  Square type."""

    def __init__(self, size=0):
        """Initialize Square with size."""
        self.__size = size
        if type(size) is not int:
            raise TypeError('size in not an integer')
        if size < 0:
            raise ValueError('size is not greater or equal 0')
