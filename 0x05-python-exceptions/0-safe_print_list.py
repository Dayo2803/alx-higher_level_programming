#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    ret = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
            ret += 1
    except Exception:
        print()
        return (ret)
    else:
        print()
        return (ret)
