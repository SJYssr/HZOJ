#!/usr/bin/env python
# coding=utf-8

n = int(input())
if n <= 3:
    print(14)
else:
    print("%.1f" % ((n - 3) * 2.3 + 14))
