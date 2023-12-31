#!/usr/bin/python3
"""Script to print tuples of square position."""


class Square:
    """Create Square type."""

    def __init__(self, dime=0, pos=(0, 0)):
        """Initialize the square with position and size."""
        self.size = dime
        try:
            self.position = pos
        except TypeError as typ:
            print(typ)

    @property
    def position(self):
        """Defines the position of the square."""
        return self.__position

    @position.setter
    def position(self, worth):
        """Define function to set the position of square."""
        if type(worth) is not tuple:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(worth) != 2:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(worth[0]) is not int or type(worth[1]) is not int:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        elif worth[0] < 0 or worth[1] < 0:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = worth

    @property
    def size(self):
        """Defines the size of square and returns its value."""
        return self.__size

    @size.setter
    def size(self, worth):
        """Define the value of size of square and checks if >= 0."""
        self.__size = worth
        if type(worth) is not int:
            raise TypeError('size must be an integer')
        if worth < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """Define the area of a square."""
        return self.__size * self.__size

    def my_print(self):
        """Print square by position."""
        if self.position:
            if self.size > 0:
                print('\n' * self.position[1], end="")
                for a in range(self.__size):
                    print(' ' * self.position[0], end="")
                    print('#' * self.size)
        if self.__size == 0:
            print()
