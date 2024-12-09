#!/usr/bin/env python
# coding=utf-8

def fbnq(n):
    if n == 1 or n == 2:
        return 1
    return fbnq(n - 1) + fbnq(n - 2)

n = int(input())
result = fbnq(n)
print(result)

