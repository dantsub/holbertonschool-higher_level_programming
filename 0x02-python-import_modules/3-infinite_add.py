#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argv = sys.argv
    if (len(argv) == 1):
        print(0)
    else:
        add = int(argv[1])
        if (len(argv) == 3):
            print(add + int(argv[2]))
        else:
            for indx in range(2, len(argv)):
                add += int(argv[indx])
            print(add)
