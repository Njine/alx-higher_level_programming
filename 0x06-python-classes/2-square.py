#!/usr/bin/python3
"class Square:
    """A class that represents a square."""

    def __init__(self, size=1):
        """
        Initialize a square with a given size.

        Args:
            size (int): The size of the square. Must be >= 0.
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
