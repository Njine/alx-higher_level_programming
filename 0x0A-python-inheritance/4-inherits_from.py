#!/usr/bin/python3
"""True if the object is an instance of a class that inherited, else False."""


def inherits_from(obj, a_class):
    """
    Return True or False and isinstance(obj, a_class)
    and not isinstance(obj, a_class).
    """
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
