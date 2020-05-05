#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    r = len(my_list)
    list = my_list[:]
    if idx < 0 or idx > r - 1:
        return (list)
    list[idx] = element
    return (list)
