#!/usr/bin/python3
def remove_char_at(str, n):
    string_cpy = ''
    for i in range(len(str)):
        if i != n:
            string_copy += str[i]
    return (string_copy)
