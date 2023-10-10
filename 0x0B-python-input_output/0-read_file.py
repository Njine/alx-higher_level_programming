#!/usr/bin/python3
"""Read a file and print to stdout."""


def read_file(filename=""):
    """Reads from a file."""
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end="")
