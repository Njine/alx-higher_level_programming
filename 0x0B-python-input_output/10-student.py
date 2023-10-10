#!/usr/bin/python3
"""Create class Student"""


class Student:
    """Student class."""
    def __init__(self, first_name, last_name, age):
        """Initialize student class."""
        self.firstName = first_name
        self.lastName = last_name
        self.studentAge = age

    def to_json(self, attrs=None):
        """Convert file to JSON."""
        if attrs is None:
            return self.__dict__
        my_dict = {}
        for items in attrs:
            if hasattr(self, items):
                my_dict[items] = getattr(self, items)
        return my_dict
