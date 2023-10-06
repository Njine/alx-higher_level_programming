#!/usr/bin/python3

"""Contain a function that adds new line after characters."""
def text_indentation(text):
    """Add two new lines to string at character points."""
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    fullStop = text.replace('.', '.\n\n')
    fullStop = fullStop.replace('?', '?\n\n')
    fullStop = fullStop.replace(':', ':\n\n')
    fullStop1 = fullStop.split('\n')
    for line in range(len(fullStop1)):
        print("{}".format(fullStop1[line].strip()),
              end=("" if (line == (len(fullStop1) - 1)) else '\n'))
