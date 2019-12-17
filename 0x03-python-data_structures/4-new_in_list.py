#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = my_list.copy()
    if (len(new) > idx or idx > -1):
        new[idx] = element
    return new
