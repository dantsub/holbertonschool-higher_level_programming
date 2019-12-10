#!/usr/bin/python3
for abc in range(122, 96, -1):
    if abc % 2 == 1:
        abc -= 32
    print('{:c}'.format(abc), end='')
