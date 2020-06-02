#!/usr/bin/python3
"""Define class Mylist"""


class MyList(list):
    """class MyList"""
    def print_sorted(self):
        """sorted list"""
        print(sorted(self))
