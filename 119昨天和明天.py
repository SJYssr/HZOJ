#!/usr/bin/env python
# coding=utf-8

def calc_day(y, m, d):
    month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (y % 4 == 0 and y % 100) or y % 400 == 0: month[2] += 1
    if d == 0:
        m -= 1
        if m == 0:
            y -= 1
            m = 12
        d = month[m]
    elif d > month[m]:
        m += 1
        if m > 12:
            y += 1
            m = 1
        d = 1
    print(y, m, d)

y, m, d = input().split()
calc_day(int(y), int(m), int(d) - 1)
calc_day(int(y), int(m), int(d) + 1)
