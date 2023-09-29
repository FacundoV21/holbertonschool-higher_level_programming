#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0
    for i in range(0, x + 1):
        try:
            print("{}".format(my_list[i]), end="")
            n += 1
        except Exception:
            break

    print()
    return n
