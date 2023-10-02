#!/usr/bin/python3
"""
    Text identation function, all of its test are located on the tests folder

"""


def text_indentation(text):
    """Function that replaces . ? and : for \n\n"""

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    result = text.replace(". ", ".\n\n")
    result = result.replace("? ", "?\n\n").replace(": ", ":\n\n")
    print(result, end="")
