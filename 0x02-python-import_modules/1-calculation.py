#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

def perform_arithmetic_operations(a, b):
    """Perform arithmetic operations on two numbers and print the results."""
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))

if __name__ == "__main__":
    a = 10
    b = 5

    perform_arithmetic_operations(a, b)
