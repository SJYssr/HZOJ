#!/usr/bin/env python
# coding=utf-8

a = input()
x = int(input())
b = input()

print(min(100, len(a)))
a = a[:x - 1] + b + a[x - 1:]
print(a)
print(len(a) - a.rfind('x'))
