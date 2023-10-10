#!/usr/bin/python3
"""Count number of lines in a file."""


def number_of_lines(filename=""):
    """Read from a file and print number of lines."""
    count = 0
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            count += 1
    return count
