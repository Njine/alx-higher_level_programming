#!/usr/bin/python3
"""Create class Student."""


class Student:
    """Student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize student class."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Convert file to JSON."""
        return self.__dict__
