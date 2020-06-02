#!/usr/bin/python3
"""inherits_form"""


def inherits_from(obj, a_class):
    """extends test
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
