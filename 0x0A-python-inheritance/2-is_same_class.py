#!/usr/bin/python3
"""Check instance of specified object."""


def is_same_class(obj, a_class):
    """See if instance is same."""
    return issubclass(a_class, type(obj))
