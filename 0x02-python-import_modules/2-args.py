#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    a = len(argv)
    print("{:d} {:s}{:s}".format(a - 1, "argument" if a <= 2 else "arguments",
    "." if a == 1 else ":"))
    for i in range(1, a):
        print('{:d}: {:s}'.format(i, argv[i]))
