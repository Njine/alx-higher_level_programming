#!/usr/bin/python3
"""Add new attribute to an object."""


def add_attribute(ob, attr, value):
    """Add attribute to class otherwise raise error."""
    if hasattr(ob, "__dict__"):
        setattr(ob, attr, value)
    else:
        raise TypeError("can't add new attribute")
