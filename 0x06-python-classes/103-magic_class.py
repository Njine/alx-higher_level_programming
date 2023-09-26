#!/usr/bin/python3
import math


class MagicClass:
    """Create a circle area class."""

    def __init__(self, radius=0):
        """Initialize."""
        self.__radius = 0
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def circumference(self):
        """Define circumference."""
        return 2 * math.pi * self.__radius

    def area(self):
        """Define area."""
        return math.pi * self.__radius ** 2
