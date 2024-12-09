#!/usr/bin/env python
# coding=utf-8

def str_replace(string, str1, str2):
    while str1 in string:
        string = string.replace(str1, str2)
    return string

str = input()
str = str_replace(str, " ", "%20")
print(str)
