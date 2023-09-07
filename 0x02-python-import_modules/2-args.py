#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]
    count = len(arguments)

    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))

    for i, arg in enumerate(arguments, start=1):
        print("{}: {}".format(i, arg))
