#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    no_change_size = dict(a_dictionary)
    for key, val in no_change_size.items():
        if val == value:
            del a_dictionary[key]
    return a_dictionary
