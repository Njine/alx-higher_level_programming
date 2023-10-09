#!/usr/bin/python3
"""Rectangle class."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle inherits from BaseGeometry"""

    class Rectangle:
    def __init__(self, width, height):
        self.__width = self.validate_and_set('width', width)
        self.__height = self.validate_and_set('height', height)

    def validate_and_set(self, name, value):
        super().integer_validator(name, value)
        return value
