#!/usr/bin/python3
from magic_calculation_102 import add, sub


def magic_calculation(a, b):
    if a < b:
        c = add(a, b)
        i = 4
        while i < 6:
            c = add(c, i)
            i += 1
        return c
    return sub(a, b)
