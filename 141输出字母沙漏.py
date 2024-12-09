#!/usr/bin/env python
# coding=utf-8

n = int(input())

for i in range(2 * n + 1):
    a_sum = 2 * abs(i - n) + 1
    b_sum = n - abs(i - n)
    ch = chr(ord('A') + n)
    for j in range(b_sum):
        print(" ", end="")
    for k in range(a_sum):
        print(chr(ord(ch) - abs(k - a_sum // 2)), end="")
    print()
