#!/usr/bin/python3
"""Return dictionary description."""


def class_to_json(obj):
    """Convert class to JSON."""
    return obj.__dict__
