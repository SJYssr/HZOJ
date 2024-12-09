#!/usr/bin/env python
# coding=utf-8

def calc(x, n):
    sum = x
    for i in range(n):
        sum = sum * (1 + 0.06)
    return sum

x, n = map(int, input().split())
result = calc(x, n)
print("%.6lf" % result)

