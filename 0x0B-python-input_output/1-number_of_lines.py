#!/usr/bin/python3
"""number_of_lines"""


def number_of_lines(filename=""):
    """number of lines of file"""
    with open(filename, 'r', encoding='utf8') as file:
        i = 0
        for l in file:
            i += 1
        return i
