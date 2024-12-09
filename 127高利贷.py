#!/usr/bin/env python
# coding=utf-8

x, n = map(int, input().split())
for i in range(n):
    x = x * (1 + 0.06)
print(int(x))
