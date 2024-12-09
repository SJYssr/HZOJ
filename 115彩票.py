#!/usr/bin/env python
# coding=utf-8

def calc_price(x, y):
    if (x == y):
        return 100
    x1 = x // 10
    x2 = x % 10
    y1 = y // 10
    y2 = y % 10
    if (x1 == y2 and x2 == y1):
        return 20
    if (x1 == y2 or x1 == y1 or x2 == y1 or x2 == y2): return 2
    return 0

x, y = input().split()
print(calc_price(int(x), int(y)))
