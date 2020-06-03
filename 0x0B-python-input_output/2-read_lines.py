#!/usr/bin/python3
"""read_lines"""


def read_lines(filename="", nb_lines=0):
    """reads n lines of a text file (UTF8) and prints it to stdout"""
    number_of_lines = __import__('1-number_of_lines').number_of_lines
    with open(filename, 'r', encoding='utf-8') as file:
        if nb_lines <= 0 or number_of_lines(filename) <= nb_lines:
            print(file.read(), end='')
            return
        i = 0
        for i, line in enumerate(file):
            if i == nb_lines:
                break
            print(line, end='')
