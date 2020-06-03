#!/usr/bin/python3
"""load_from_json_file"""


import json


def load_from_json_file(filename):
    """load from JSON file"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
