#!/usr/bin/python3
"""Defines a function to to_JSON_string."""
import json


def to_json_string(my_obj):
    """Returns JSON rep of an obj.
    Args:
        1. my_obj: An object.
    """
    return json.dumps(my_obj)
