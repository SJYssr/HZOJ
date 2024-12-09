#!/usr/bin/env python
# coding=utf-8

n = int(input())
for i in range(2 * n + 1):
    for p in range(n - abs(i - n)):
        print(" ", end="")
    for p in range(2 * abs(i - n) + 1):
        if p == 0 or p == 2 * abs(i - n):
            print(abs(i - n), end="")
        else:
            print(" ", end="")
    print()
