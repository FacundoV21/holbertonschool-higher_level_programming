#!/usr/bin/python3
def uniq_add(my_list=[]):
    already_in = []
    result = 0
    for i in range(1, len(my_list)):
        if my_list[i] not in already_in:
            already_in.append(my_list[i])
            result += my_list[i]
    return result
