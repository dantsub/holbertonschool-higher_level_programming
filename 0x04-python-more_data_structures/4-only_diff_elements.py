#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    one, sec = set(set_1), set(set_2)
    return one ^ sec
