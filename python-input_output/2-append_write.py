#!/usr/bin/python3
"""
    Start of the program
"""


def append_write(filename="", text=""):
    """
        Function to append text into a file
    """
    with open(filename, 'a', encoding="utf-8") as f:
        num = f.write(text)
    
    return num
