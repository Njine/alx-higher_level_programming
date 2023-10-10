#!/usr/bin/python3
"""Return an object by a JSON representation."""
import json


def from_json_string(my_str):
    """Convert from JSON to python."""
    return json.loads(my_str)
