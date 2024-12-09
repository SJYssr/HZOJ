#!/usr/bin/env python
# coding=utf-8

def check_data(y, m, d):
    if m <= 0 or m > 12 or d <= 0 or d > 31: return False
    month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (y % 4 == 0 and y % 100) or y % 400 == 0: month[2] += 1
    return d <= month[m]


y, m, d = input().split()
print("YES" if check_data(int(y), int(m), int(d)) else "NO")
