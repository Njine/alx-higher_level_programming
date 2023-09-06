#!/usr/bin/python3
# 8-uppercase.py

def uppercase(s):
    """Print a string in uppercase followed by a new line."""
    for c in s:
        if 'a' <= c <= 'z':
            c = chr(ord(c) - 32)
        print(f"{c}", end="")
    print("")
