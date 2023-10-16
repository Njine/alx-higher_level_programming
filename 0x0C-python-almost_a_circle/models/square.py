#!/usr/bin/python3
""" Module that contains class Square,
inheritance of class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes instances """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ str special method """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """ Getter for size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update method """
        attrs = ['id', 'size', 'x', 'y']
        if args:
            for i, arg in enumerate(args):
                if attrs[i] == 'size':
                    self.width = arg
                    self.height = arg
                else:
                    setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    self.width = value
                    self.height = value
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns a dictionary with attributes """
        attrs = ['id', 'size', 'x', 'y']
        return {key: (self.width if key == 'size' else getattr(self, key)) for key in attrs}
