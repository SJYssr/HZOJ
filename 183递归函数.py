#!/usr/bin/env python
# coding=utf-8

def f(x):
    if x <= 0:
        return 0
    elif x == 1:
        return 1
    elif x % 2 == 0:
        return 3 * f(x // 2) - 1
    else:
        return 3 * f((x + 1) // 2) - 1

n = int(input())
result = f(n)
print(result)

