#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        inf = (0, None)
    else:
        inf = (len(sentence), sentence[0])

    return inf
