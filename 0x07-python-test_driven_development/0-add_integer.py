#!/usr/bin/python3
"""
This Module is the function that adds of two number
"""


def add_integer(a, b=98):
    """Returns an integer: the addition of a and b"""
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a + b)
