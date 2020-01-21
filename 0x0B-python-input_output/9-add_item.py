#!/usr/bin/python3
"""
Load, add, save module
"""
from sys import argv
save_json = __import__('7-save_to_json_file').save_to_json_file
load_json = __import__('8-load_from_json_file').load_from_json_file

lis = argv[1:]
try:
    before = load_json('add_item.json')
except IOError:
    before = []
save_json(before + lis, 'add_item.json')
