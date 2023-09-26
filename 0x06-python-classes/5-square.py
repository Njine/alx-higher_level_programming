#!/usr/bin/python3
"""Prints to stdout the square with the character # ."""


class Square:
    """Create Square type."""

    def __init__(self, dime=0):
        """Initialize Square with size."""
        self.size = dime

    @property
    def dime(self):
        """Define size of square and returns value."""
        return self.__size

    @dime.setter
    def dime(self, worth):
        """Define the value of size of square and checks if >= 0."""
        self.__size = worth
        if type(worth) is not int:
            raise TypeError('size must be an integer')
        if worth < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """Define area of a square."""
        return self.__size * self.__size

    def my_print(self):
        """Print in stdout the square with character #."""
        for a in range(self.__size):
            for b in range(self.__size):
                print('#', end="")
            print()
        if self.__size == 0:
            print()
