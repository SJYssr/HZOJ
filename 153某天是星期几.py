#!/usr/bin/env python
# coding=utf-8

week = [6, 7, 1, 2, 3, 4, 5]

def get_weekday(y, m, d):
    if m == 1 or m == 2:
        m += 12
        y -= 1
    j = y // 100
    k = y % 100
    h = (d + 26 * (m + 1) // 10 + k + k // 4 + j // 4 + 5 * j) % 7
    return week[h]

y, m, d = map(int, input().split())
print(get_weekday(y, m, d))

