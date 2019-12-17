#!/usr/bin/python3
def element_at(my_list, idx):
    return None if (len(my_list) < idx or idx < 0) else my_list[idx]
