#!/usr/bin/python3
for first in range(0, 10):
    second = first + 1
    for second in range(0, 10, 1):
        if (first != 8 or second != 9):
            if (first != 8 and second > first):
                print('{}{}'.format(first, second), end=', ')
        else:
            print('{}{}'.format(first, second))
