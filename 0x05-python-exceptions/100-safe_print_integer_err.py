#!/usr/bin/python3
from sys import stderr

def safe_print_integer_err(value):
    try:
        value_int = int(value)
        print("{:d}".format(value_int))
        return True
    except (ValueError, TypeError):
        stderr.write("Exception: {}\n".format("unsupported operand type"))
        return False
