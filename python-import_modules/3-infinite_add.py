#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = 0
    for i in range(1, len(sys.argv)):
        n = n + int(sys.argv[i])

    print("{}".format(n))
