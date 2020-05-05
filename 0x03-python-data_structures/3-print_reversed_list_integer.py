#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        list = reversed(my_list)
        for x in list:
            print('{:d}'.format(x))
