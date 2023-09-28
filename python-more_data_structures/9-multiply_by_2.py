#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multyplied = dict()

    for key, value in a_dictionary.items():
        multyplied[key] = value * 2
    return multyplied
