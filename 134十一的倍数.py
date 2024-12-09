#!/usr/bin/env python
# coding=utf-8

a, b = map(int, input().split())
x_str = ""
for i in range(a, b + 1):
    if i % 11: continue
    x_str += str(i) + ' '
x_str = x_str[:-1]
print(x_str)
