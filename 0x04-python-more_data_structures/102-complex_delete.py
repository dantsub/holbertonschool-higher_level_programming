#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key = [k for k, val in a_dictionary.items() if val == value]
    if key:
        for element in key:
            del a_dictionary[element]
    return a_dictionary
