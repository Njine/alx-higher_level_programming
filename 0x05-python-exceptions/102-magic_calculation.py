#!/usr/bin/python3
def magic_calculation(a, b):
    try:
        if a > 1:
            result = a ** b / (a - 1)
        else:
            raise ValueError('Too far')
    except ValueError:
        result = b + a
    return result
