#!/usr/bin/python3
"""Defines a function append_write."""


def append_write(filename="", text=""):
    """Returns number of characters appended to filename.
    Args:
        1. filename: Name of the file to append to.
        2. text: Text to append to filename.
    """
    with open(filename, "a+", encoding="utf-8") as fl:
        return fl.write(text)
