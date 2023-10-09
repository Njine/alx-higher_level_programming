#!/usr/bin/python3
"""Class with public instance; Raise exception apropriately."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square; inherits from rectangle."""

    def __init__(self, size):
        """Class instantiation."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
