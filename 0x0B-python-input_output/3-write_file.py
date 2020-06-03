#!/usr/bin/python3
"""wrtie_file"""


def write_file(filename="", text=""):
    """open and write"""
    with open(filename, 'w', encoding='utf=8') as file:
        return file.write(text)
