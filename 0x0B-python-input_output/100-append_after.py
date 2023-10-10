#!/usr/bin/python3
"""Append a line."""


def append_after(filename="", search_string="", new_string=""):
    """Add a new line when a string is found."""
    updated_lines = []

    with open(filename, 'r', encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            updated_lines.append(line)
            if search_string in line:
                updated_lines.append(new_string)

    with open(filename, 'w', encoding="utf-8") as file:
        file.writelines(updated_lines)
