#!/usr/bin/env python
# coding=utf-8

def get_days(y, m):
    month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (y % 4 == 0 and y % 100) or y % 400 == 0:
        month[2] += 1
    return month[m]

y, m = input().split()
print(get_days(int(y), int(m)))
