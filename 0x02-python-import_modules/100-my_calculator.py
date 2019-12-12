#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    from calculator_1 import add, sub, mul, div
    operator = [['+', add], ['-', sub], ['*', mul], ['/', div]]
    if (len(argv) < 4):
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    arg1 = int(argv[1])
    arg2 = int(argv[3])
    for op in operator:
        if (argv[2] == op[0]):
            print('{} {} {} = {}'.format(arg1, op[0], arg2, op[1](arg1, arg2)))
            exit(0)
    print('Unknown operator. Available operators: +, -, * and /')
    exit(1)
