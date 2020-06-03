#!/usr/bin/python3
"""
inserts a line of text to a file, after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """append_after"""
    list = []
    with open(filename, 'r', encoding='utf-8') as file:
        while 1 == 1:
            line = file.readline()
            if line == '':
                break
            list.append(line)
            if search_string in line:
                list.append(new_string)
    with open(filename, 'w', encoding='utf-8') as file_w:
        file_w.writelines(list)
