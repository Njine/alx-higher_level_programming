#!/usr/bin/python3
"""Return JSON representation of an object."""
import json


def to_json_string(my_obj):
    """Converter from python to JSON."""
    return json.dumps(my_obj)
