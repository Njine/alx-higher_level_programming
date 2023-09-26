#!/usr/bin/python3
from sys import stderr

def safe_print_integer_err(value):
    success = False
    i = 0

    while not success and i < 1:
        try:
            integer_value = int(value)
            print("{:d}".format(integer_value))
            success = True
        except (ValueError, TypeError):
            stderr.write("Exception: {}\n".format("unsupported operand type"))
            i += 1

    return success
