#!/usr/bin/python3

# Import the BaseGeometry class from the 7-base_geometry module
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """A class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a Rectangle instance with width and height."""
        # Call the integer_validator method from the parent class for width
        super().integer_validator('width', width)
        # Assign the width as a private instance attribute
        self.__width = width
        # Call the integer_validator method from the parent class for height
        super().integer_validator('height', height)
        # Assign the height as a private instance attribute
        self.__height = height

    def __str__(self):
        """Return an informal representation of the Rectangle."""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def __repr__(self):
        """Return a formal representation of the Rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Compute and return the area of the Rectangle."""
        return self.__width * self.__height
