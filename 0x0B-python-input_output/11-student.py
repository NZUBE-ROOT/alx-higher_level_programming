#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Initialization of the class."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Rtrieves a dictionary representation of a Student instance.
        Args:
            1. attrs: The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(att) == str for att in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student.
        Args:
            1. json: The key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
