#!/usr/bin/python3
"""Python script defines a square, private attribute of size."""


class Square:
    """Makes Square type."""

    def __init__(self, dimension):
        """Initialize Square with size."""
        self.__size = dimension
