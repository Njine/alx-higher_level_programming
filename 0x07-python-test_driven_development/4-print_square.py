#!/usr/bin/python3

"""Contain a function that prints square by size input."""


def print_square(size):

    """Python function that prints square '#' by size variable."""

    if not isinstance(size, int):
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')

    for rows in range(size):
        for cols in range(size):
            print('#', end='')
        print()
