#!/usr/bin/env python
# coding=utf-8

numbers = list(map(int, input().split()))
numbers.sort(reverse = True)

x_str = ""
for i in numbers:
    x_str += str(i) + " "
print(x_str[:-1])
