#!/usr/bin/env python
# coding=utf-8

ch = 0
num = 0
space = 0
other = 0

x_str = input()
for i in x_str:
    if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
        ch += 1
    elif i == ' ':
        space += 1
    elif i >= '0' and i <= '9':
        num += 1
    else:
        other += 1
print(ch, num, space, other)

