#!/usr/bin/env python
# coding=utf-8

def f(n, a):
    sum_val = 0
    i = 1
    size = 0
    while sum_val < n:
        sum_val += a[i]
        i += a[i]
        size += 1
    return size

n = int(input())
a = [0] + list(map(int, input().split()))  # Add a dummy element at index 0
result = f(n, a)
print(result)

