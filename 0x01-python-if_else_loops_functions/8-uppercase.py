#!/usr/bin/python3
# 8-uppercase.py

def uppercase(s):
    """Print a string in uppercase followed by a new line."""
    uppercase_str = ""
    for c in s:
        if ord('a') <= ord(c) <= ord('z'):
            c = chr(ord(c) - 32)
        uppercase_str += c
    print("{}".format(uppercase_str))
