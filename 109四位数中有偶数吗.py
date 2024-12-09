#!/usr/bin/env python
# coding=utf-8

def is_val(n):
    while n:
        if n % 10 % 2 == 0:
            return True
        n //= 10
    return False

n = int(input())
print("%s" % (is_val(n) and "YES" or "NO"))
