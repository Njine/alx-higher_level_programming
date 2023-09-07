#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(argv) != 4:
        print('Usage: {} <a> <operator> <b>'.format(argv[0]))
        exit(1)

    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])

    ops = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }

    if operator in ops:
        result = ops[operator](a, b)
        print('{:d} {:s} {:d} = {:d}'.format(a, operator, b, result))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
