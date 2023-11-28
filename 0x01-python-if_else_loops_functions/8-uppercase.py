#!/usr/bin/python
def uppercase(str):
    for ic in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end='')
    print("", end='\n')
