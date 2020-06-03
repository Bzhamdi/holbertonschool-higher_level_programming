#!/usr/bin/python3
"""save_to_json_file"""

import json


def save_to_json_file(my_obj, filename):
    """save object to jason file"""
    with open(filename, 'w', encoding='utf-8') as file:
        return json.dump(my_obj, file)
