#!/usr/bin/python3
"""
    function to return true or false depending on 2 factors
"""


def is_kind_of_class(obj, a_class):
    """
        Return true if the obj is a instance of class or subclass
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
