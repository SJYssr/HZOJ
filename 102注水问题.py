#!/usr/bin/env python
# coding=utf-8

a, b, c, t = input().split()
a = float(a)
b = float(b)
c = float(c)
t = float(t)
print("%.2f" % ((1 - (1 / a + 1 / b) * t) / (1 / a  + 1 / b - 1 / c) + t))
