#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = len(tuple_a)
    b = len(tuple_b)
    if a >= 1:
        a1 = tuple_a[0]
    else:
        a1 = 0
    if b >= 1:
        b1 = tuple_b[0]
    else:
        b1 = 0
    if a >= 2:
        a2 = tuple_a[1]
    else:
        a2 = 0
    if b >= 2:
        b2 = tuple_b[1]
    else:
        b2 = 0
    new = (a1 + b1, a2 + b2)
    return (new)
