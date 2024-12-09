#!/usr/bin/env python
# coding=utf-8

pi = 3.14
r, h = input().split(' ')
r = float(r)
h = float(h)
print("%.2f" % (r * r * pi), "%.2f" % (r * r * pi * h), sep = '\n')
