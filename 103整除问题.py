#!/usr/bin/env python
# coding=utf-8

a, b = input().split()
print("%s" % (int(a) % int(b) == 0 and "YES" or "NO"))
