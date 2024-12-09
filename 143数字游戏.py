#!/usr/bin/env python
# coding=utf-8

import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def func(x):
    return x * x

def binary_search(func, n):
    head = 1
    tail = n
    while head <= tail:
        mid = (head + tail) // 2
        if func(mid) == n:
            return True
        if func(mid) < n:
            head = mid + 1
        else:
            tail = mid - 1
    return False

def check_sqrt(n):
    return binary_search(func, n)

def is_val(n):
    return (n % 6 == 0) and is_prime(n // 100) and check_sqrt(n % 100)

a, b = map(int, input().split())
cnt = 0

for i in range(a, b + 1):
    if not is_val(i):
        continue
    if cnt > 0:
        print(" ", end="")
    print(i, end="")
    cnt += 1

print()
print(cnt)
