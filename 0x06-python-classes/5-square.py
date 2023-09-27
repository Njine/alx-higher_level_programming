#!/usr/bin/python3
"""Print to stdout the square with the character # ."""


class Square:
    """Create  Square type."""

    def __init__(self, dime=0):
        """Initialize Square with size."""
        self.size = dime

    @property
    def size(self):
        """Define the size of square and returns its value."""
        return self.__size

    @size.setter
    def size(self, param):
        """Set the value of size for the square and check if it's >= 0."""
        if not isinstance(param, int):
            raise TypeError('Size must be an integer')
        if param < 0:
            raise ValueError('Size must be >= 0')
        self.__size = param

    def area(self):
        """Define the area of a square."""
        return self.__size * self.__size

    def my_print(self):
        """Print in stdout the square with character #."""
        for a in range(self.__size):
            for b in range(self.__size):
                print('#', end="")
            print()
        if self.__size == 0:
            print()
