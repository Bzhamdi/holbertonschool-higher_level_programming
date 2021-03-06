#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    div, r = 0, 0
    for x in my_list:
        r += x[0] * x[1]
        div += x[1]
    return (r / div)
