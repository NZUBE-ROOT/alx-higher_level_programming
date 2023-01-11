#!/usr/bin/python3
"""Defines a function class_to_json."""


def class_to_json(obj):
    """Returns dictionary description with simple data str.
    Args:
        1. obj: Instance of a class.
    """
    return obj.__dict__
