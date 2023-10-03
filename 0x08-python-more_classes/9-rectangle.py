#!/usr/bin/python3

"""Define Rectangle type."""


class Rectangle:
    """Define the Rectangle type."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Return a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle_str = ""
            for h in range(self.__height):
                rectangle_str += str(self.print_symbol) * self.__width
                if h < self.__height - 1:
                    rectangle_str += "\n"
            return rectangle_str

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare rectangles and get one with greater or equal area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __repr__(self):
        """Return a string representation of the rectangle for object."""
        return "Rectangle({}, {})".format(self.width, self.height)

    def area(self):
        """Get the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Get the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.height + self.width)

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
        """Destructor method called when an instance is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @classmethod
    def square(cls, size=0):
        """Create a square Rectangle with equal width and height."""
        return cls(size, size)  # Use the class (cls) to create a square

    @property
    def print_symbol(self):
        """Get the print_symbol for the rectangle."""
        return self.__print_symbol

    @print_symbol.setter
    def print_symbol(self, value):
        """Set the print_symbol for the rectangle."""
        self.__print_symbol = value
