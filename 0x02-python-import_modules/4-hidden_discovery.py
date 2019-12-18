#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    list1 = dir(hidden_4)
    for item in list1:
        if (item[0] != '_'):
            print(item)
