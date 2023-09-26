#!/usr/bin/python3
"""Define area that returns the current square area."""


class Square:
    """Create Square type."""

    def __init__(self, dime=0):
        """Initialize Square with size."""
        self.size = dime

    @property
    def size(self):
        """Define the size of square, return value."""
        return self.__size

    @size.setter
    def size(self, worth):
        """Set the value of size and check if it's >= 0."""
        if type(worth) is not int:
            raise TypeError('size must be an integer')
        if worth < 0:
            raise ValueError('size must be >= 0')
        self.__size = worth

    def area(self):
        """Define the area of a square."""
        return self.__size * self.__size
