#!/usr/bin/python3
"""Rectangle class Module, Base class inherit."""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize instances."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width getter."""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Height getter."""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """X getter."""
        return self.__x

    @x.setter
    def x(self, value):
        """X setter."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Y getter."""
        return self.__y

    @y.setter
    def y(self, value):
        """Y setter."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle object."""
        return self.width * self.height

    def display(self):
        """Display a rectangle."""
        rectangle = "\n" * self.y + "\n".join([" " * self.x + "#" * self.width] * self.height)
        print(rectangle, end='')

    def __str__(self):
        """Str special method."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Update method."""
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Method that returns a dictionary with properties."""
        attrs = ['id', 'width', 'height', 'x', 'y']
        return {key: getattr(self, key) for key in attrs}
