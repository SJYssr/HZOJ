#!/usr/bin/env python
# coding=utf-8

def reverse_string(string):
    return string[::-1]

str_input = input()
reversed_str = reverse_string(str_input)
print(reversed_str)
