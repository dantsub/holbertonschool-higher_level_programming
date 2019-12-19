#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    for element in my_list:
        new.append(element)
        if element == search:
            new.append(replace)
    return new
