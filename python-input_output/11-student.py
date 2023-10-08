#!/usr/bin/python3
"""
    Start of the program
"""


class Student():
    """
        Creation of the class student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if not isinstance(attrs, list):
            return self.__dict__

        a = {}
        for i in attrs:
            if i in self.__dict__:
                a[i] = self.__dict__[i]
        return a

    def reload_from_json(self, json):
        for i in json:
            for j in self.__dict__:
                self.__dict__[i] = json[i]
