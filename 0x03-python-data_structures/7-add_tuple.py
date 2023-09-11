#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples have at least 2 elements by padding them with 0 if necessary
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    # Perform element-wise addition and return the result as a tuple
    return tuple(map(lambda x, y: x + y, tuple_a[:2], tuple_b[:2]))
