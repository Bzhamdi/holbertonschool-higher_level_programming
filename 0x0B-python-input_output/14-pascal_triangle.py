#!/usr/bin/python3
"""
pascal_triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers
    representing the Pascals triangle of n
    [1]
    [1,1]
    [1,2,1]
    [1,3,3,1]
    [1,4,6,4,1]
    """
    if n <= 0:
        return []
    box = []
    box.append([1])
    box.append([1, 1])
    for i in range(1, n - 1):
        case = []
        case.append(1)
        for j in range(0, len(box[-1]) - 1):
            case.append(box[-1][j] + box[-1][j + 1])
        case.append(1)
        box.append(case)
    return box
