#!/usr/bin/env python
# coding=utf-8

def sum(n):
    if n == 1:
        return 1
    else:
        return sum(n - 1) * 2 + n

def sum1(n):
    if n == 1:
        return 1
    else:
        return sum1(n - 1) * 2 + 1

n = int(input())
result1 = sum1(n)
result2 = sum(n)
print(result1, result2)

