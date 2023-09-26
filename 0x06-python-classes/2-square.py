#!/usr/bin/python3
"""2-square.py: Defines size as an int and also greater or equal to 0."""


class Square:
    """Creates  Square type."""

    def __init__(self, dimention=0):
        """Initialize Square with size."""
        self.__dimention = dimention
        if type(dimention) is not int:
            raise TypeError('size must be an integer')
        if dimention < 0:
            raise ValueError('size must be >= 0')
