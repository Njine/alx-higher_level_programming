#!/usr/bin/python3
"""Count number of lines in a file."""


def number_of_lines(filename=""):
    """Count the number of lines in a file."""
    count = 0

    with open(filename, "r", encoding="utf-8") as file:
        for _ in file:
            count += 1

    return count

