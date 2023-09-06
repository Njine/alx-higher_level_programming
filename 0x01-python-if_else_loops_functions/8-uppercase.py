#!/usr/bin/python3
# 8-uppercase.py

def uppercase(s):
    """Print a string in uppercase followed by a new line."""
    result = ""
    for c in s:
        if 'a' <= c <= 'z':
            result += chr(ord(c) - 32)
        else:
            result += c

    print(result)