#!/usr/bin/env python
# coding=utf-8

def check(n):
    while (n):
        if (n % 10 == 9):
            return True
        n //= 10
    return False

n = int(input())
print("%s" % (check(n) and "YES" or "NO"))
