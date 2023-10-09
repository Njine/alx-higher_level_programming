#!/usr/bin/python3
"""Inherit from list class."""


class MyList(list):
    """Inheritance class."""

    def print_sorted(self):
        """Print sorted list."""
        print(sorted(self))
