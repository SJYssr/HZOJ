#!/usr/bin/env python
# coding=utf-8

a, b = input().split()
c, d = input().split()
a, b, c, d = int(a), int(b), int(c), int(d)
if (a <= c and b >= d) or (a >= c and b <= d):
    print('YES')
else:
    print('NO')
