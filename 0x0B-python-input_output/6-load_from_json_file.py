#!/usr/bin/python3
"""Defines a function load_from_json_file."""
import json


def load_from_json_file(filename):
    """Creates an object from json file.
    Args:
        1. filename: Name of json file.
    """
    with open(filename, encoding="utf-8") as fl:
        return json.load(fl)
