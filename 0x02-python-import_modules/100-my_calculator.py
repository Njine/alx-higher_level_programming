#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

def main():
    if len(sys.argv) != 4:
        print('Usage: {} <a> <operator> <b>'.format(sys.argv[0]))
        sys.exit(1)

    num1 = int(sys.argv[1])
    operator = sys.argv[2]
    num2 = int(sys.argv[3])

    ops = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }

    if operator in ops:
        result = ops[operator](num1, num2)
        print('{:d} {:s} {:d} = {:d}'.format(num1, operator, num2, result))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)

if __name__ == "__main__":
    main()
