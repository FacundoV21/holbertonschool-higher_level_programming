#!/usr/bin/python3
def best_score(a_dictionary):

    if not a_dictionary:
        return None

    Big_score = list(a_dictionary.values())[0]
    keyR = list(a_dictionary.keys())[0]

    for key, value in a_dictionary.items():
        if value > Big_score:
            Big_score = value
            keyR = key
    return keyR
