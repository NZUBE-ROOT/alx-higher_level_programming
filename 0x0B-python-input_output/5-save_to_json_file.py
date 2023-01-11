#!/usr/bin/python3
"""Defines a function save_to_json_file."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a textfile using JSON rep.
    Args:
        1. my_obj: Object
        2. filename: Name of a file to write on.
    """
    with open(filename, "w") as fl:
        json.dump(my_obj, fl)
