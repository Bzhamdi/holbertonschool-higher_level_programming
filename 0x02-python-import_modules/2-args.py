#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    a = len(argv)
    if a == 1:
        print('{} arguments.'.format(a - 1))
    elif a == 2:
        print('{} argument:'.format(a - 1))
    else:
        print('{} arguments:'.format(a - 1))
    for i in range(1, a):
        print('{:d}: {:s}'.format(i, argv[i]))
