#!/usr/bin/env python
# coding=utf-8

def convert(c):
    if 'A' <= c <= 'Z':
        return chr(ord(c) + 32)
    else:
        return chr(ord(c) - 32)

str = input()
converted_str = ''.join([convert(c) for c in str])
print(converted_str)

