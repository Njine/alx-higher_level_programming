#!/usr/bin/python3
"""BaseGeometry inheritor"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherit from BaseGeometry"""

    def __init__(self, width=0, height=0):
        """Validate type with integer_validator."""
        super().integer_validator('width', width)
        self.__width = width
        super().integer_validator('height', height)
        self.__height = height

    def __str__(self):
        """Informal representation of a Rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def __repr__(self):
        """Formal representation of a Rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Calculate the area of the Rectangle"""
        return self.__width * self.__height
