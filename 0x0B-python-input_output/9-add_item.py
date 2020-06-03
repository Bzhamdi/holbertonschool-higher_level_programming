#!/usr/bin/python3
"""
script that adds all arguments to a Python list, and then save them to a file
"""
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
try:
    jason_file = load_from_json_file("add_item.json")
except:
    jason_file = []
    save_to_json_file(jason_file, "add_item.json")
for i in sys.argv[1:]:
    jason_file.append(i)
save_to_json_file(jason_file, "add_item.json")
