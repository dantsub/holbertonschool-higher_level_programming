#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = my_list.copy()
    if (len(new) > idx or idx > 0):
        new[idx] = element
    return new
