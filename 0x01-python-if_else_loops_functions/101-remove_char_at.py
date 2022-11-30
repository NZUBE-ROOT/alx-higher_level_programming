#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ''
    for k in range(len(str)):
        if k != n:
            new_str += str[k]
    return new_str
