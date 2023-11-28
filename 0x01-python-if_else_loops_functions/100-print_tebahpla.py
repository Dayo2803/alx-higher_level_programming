#!/usr/bin/python3
small = True
for i in range(122, 96, -1):
    if small:
        print("{}".format(chr(i)), end='')
        small = False
    else:
        print("{}".format(chr(i - 32)), end='')
        small = True
