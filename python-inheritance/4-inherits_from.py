#!/usr/bin/python3
"""
    function to return true or false depending the obj
    being an instance of a class
"""


def inherits_from(obj, a_class):
    """
    function to return true or false depending the obj
    being an instance of a class
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
