#!/usr/bin/python3
"""
    Module to declare list of available attributes and methods of an object
"""


def is_same_class(obj, a_class):
    """
        returns true or false depending if an obj is instance of a_class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
