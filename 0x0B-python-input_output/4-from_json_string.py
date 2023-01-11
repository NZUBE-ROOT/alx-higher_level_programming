#!/usr/bin/python3
"""Defines a function from_json_string."""
import json


def from_json_string(my_str):
    """Returns an object represented by JSON string.
    Args:
        1. my_str: JSON rep to be converted to an object.
    """
    return json.loads(my_str)
