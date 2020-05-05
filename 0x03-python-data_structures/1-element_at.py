#!/usr/bin/python3
def element_at(my_list, idx):
    r = len(my_list)
    if idx < 0 or idx > r:
        return (None)
    for x in range(r):
        if x == idx:
            return(my_list[x])
