#!/usr/bin/python3
"""Defines a function append after."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of txt after each line containg a str.
    Args:
        1. filename: Name of the file to modify.
        2. search_string: The string to be searched.
        3. new_string: New string to add.
    """
    text = ""
    with open(filename) as fl:
        for line in fl:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as fw:
        fw.write(text)
