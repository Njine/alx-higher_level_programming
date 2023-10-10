#!/usr/bin/python3
"""Create class Student."""


class Student:
    """Student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize student class."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Convert object attributes to JSON."""
        if attrs is None:
            return self.__dict__
        return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """Reload object attributes from JSON dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
