#!/usr/bin/env python
# coding=utf-8

def peach(k, n):
    if k == n:
        return 1
    return (peach(k + 1, n) + 1) << 1

n = int(input())
result = peach(1, n)
print(result)

