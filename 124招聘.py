#!/usr/bin/env python
# coding=utf-8

def check(a, b, c, d):
    return (b <= 50 or a >= 1) and (c <= 25 or d >= 5)

a, b, c, d = input().split()
a, b, c, d = int(a), int(b), int(c), int(d)
print("ok" if check(a, b, c, d) else 'pass')
