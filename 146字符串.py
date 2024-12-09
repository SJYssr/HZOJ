#!/usr/bin/env python
# coding=utf-8

str_input = input()
result = ""

for char in str_input:
    if char == 'z':
        result += 'a'
    elif char == 'Z':
        result += 'A'
    elif 'a' <= char <= 'z':
        result += chr(ord(char) + 1)
    elif 'A' <= char <= 'Z':
        result += chr(ord(char) + 1)
    else:
        result += char

print(result)

