#!/usr/bin/env python
# coding=utf-8

a = input()
n = int(input())
b = input()

print(len(a))
print(a.find('a') + 1)
a = a[:n - 1] + b + a[n - 1:]
print(a)

