#!/usr/bin/python3

"""class Rectangle that defines a rectangle."""


class Rectangle:
    """Define the Rectangle type."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance."""
        self.width = width
        self.height = height

    def __str__(self):
        """Return a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle_str = ""
            for h in range(self.__height):
                rectangle_str += '#' * self.__width
                if h < self.__height - 1:
                    rectangle_str += "\n"
            return rectangle_str

    def __repr__(self):
        """Return a string representation of the rectangle for object."""
        return ("Rectangle({}, {})".format(self.width, self.height))

    def area(self):
        """Get the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Get the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (2 * (self.height + self.width))

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def __del__(self):
        """Destructor method called when instance is deleted."""
        print("Bye rectangle...")
