#!/usr/bin/python3
def element_at(my_list, idx):
    return None if (len(my_list) - 1 < idx or idx < 0) else my_list[idx]
