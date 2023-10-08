#!/usr/bin/python3
"""
    Start of the program
"""


def class_to_json(obj):
    """
        Returns the dictionary description with simple data structure
    """
    a = obj.__dict__

    for key, i in a.items():
        if isinstance(i, (list, dict, str, int, bool)):
            a[key] = i
    return a
