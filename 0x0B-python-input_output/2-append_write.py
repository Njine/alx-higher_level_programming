#!/usr/bin/python3
"""Append string to a file."""


def append_write(filename="", text=""):
    """Add file content, if does not exist then is created."""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
