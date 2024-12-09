#!/usr/bin/env python
# coding=utf-8

ch = input()
m, n = input().split()
S = float(m) * float(n)
print("%.2f" % (S if ch == 'r' else S / 2))
