#!/usr/bin/python3
def uppercase(str):
    i = 0
    for i in str:
        letter = i
        if (ord(i) >= 96 and ord(i) <= 123):
            letter = chr(ord(i) - 32)

        print("{}".format(letter), end="")
    else:
        print()
