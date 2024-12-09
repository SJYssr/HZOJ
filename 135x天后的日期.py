#!/usr/bin/env python
# coding=utf-8

def solve(y, m, d):
    month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (y % 4 == 0 and y % 100) or y % 400 == 0: month[2] += 1
    if d > month[m]:
        d -= month[m]
        m += 1
    if m > 12: y, m = y + 1, 1
    return y, m, d

x = int(input())
y, m, d = map(int, input().split())
for i in range(1, x + 1):
    y, m, d = solve(y, m, d + 1)
print(y, m, d)
