#!/usr/bin/python3
"""append_wrtie"""


def append_write(filename="", text=""):
    """open and append if file exit else create new file"""
    with open(filename, 'a', encoding='utf=8') as file:
        return file.write(text)
