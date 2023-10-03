#!/usr/bin/python3


"""
   0-add_integer function

   Contains a function that adds two integers
"""


def add_integer(a, b=98):
    """Add two integers.

    :param a: The first integer or float.
    :param b: The second integer or float (default is 98).
    :return: The sum of a and b as an integer.
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer or float")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer or float")

    a = int(a)
    b = int(b)

    return a + b
