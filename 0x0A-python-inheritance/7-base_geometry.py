#!/usr/bin/python3
"""
Module contains a class
with public instance, give
exception if required
"""


class BaseGeometry:
    """Has two public instances."""

    def __init__(self):
        """Initialize class."""
        pass

    def area(self):
        """Raise an exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        See if value input is correct type/validate value.
        else isinstance(value, int):
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
