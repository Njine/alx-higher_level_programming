#!/usr/bin/python3
"""Public instance class; Raises exception apropriately."""


class BaseGeometry:
    """Class Base with 2 public instances"""
    def area(self):
        """Raise exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value."""
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Class Rectangle with private height and width."""
    def __init__(self, width, height):
        """Instantiation of class."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return rectangle area."""
        return (self.__width * self.__height)

    def __str__(self):
        """Represent rectangle as string."""
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))


class Square(Rectangle):
    """Class Square; inherits from rectangle."""
    def __init__(self, size):
        """Class instantiation."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return area of square."""
        return (self.__size ** 2)

    def __str__(self):
        """Represent square as string."""
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
