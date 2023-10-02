#!/usr/bin/python3

"""define Rectangle type."""


class Rectangle:
    """Define the Rectangle type."""

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height

    def __str__(self):
        """Return a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return
        else:
            for h in range(self.__height):
                for w in range(self.height - 1):
                    print('#' * self.__width)
                return '#' * self.width

    def area(self):
        """Define area of rectange."""
        return self.width * self.height

    def perimeter(self):
        """Define perimeter of rectange."""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (2 * (self.height + self.width))

    @property
    def width(self):
        """Define width of rectange."""
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
        """Define height of rectange."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
