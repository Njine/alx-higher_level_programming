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
        """Define the value of size of square and checks if >= 0."""
        self.__size = param
        if type(param) is not int:
            raise TypeError('size must be an integer')
        if param < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """Define the area of a square."""
        return self.__size * self.__size

    def my_print(self):
    """Print in stdout the square with character #."""
    if self.__size == 0:
        print()
    else:
        for _ in range(self.__size):
            print('#' * self.__size)
